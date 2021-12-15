import json

file = open('input.txt', 'r')
input_file = file.read().splitlines()

template = input_file[0]
rules = {}
for line in input_file[2:]:
    pair = line.split()[0]
    output = line.split()[2]
    rules[pair] = output


def process(template:str, rules:map, steps:int):
    slow_index = 0
    fast_index = 1

    # stores occurrences of each pair
    polymer_pairs = {}

    # initialize polymer_pairs dict with initial template
    while fast_index < len(template):
        pair = template[slow_index] + template[fast_index]
        num = polymer_pairs.get(pair, 0)
        polymer_pairs[pair] = num + 1
        slow_index += 1
        fast_index += 1

    # stores occurences of each character
    element_occurrences = {}

    # initialize element_occurrences for initial template
    for element in template:
        element_occurrences[element] = element_occurrences.get(element, 0) + 1
    
    for step in range(steps):
        new_pairs = {}
        # for each pair in ruleset:
        #   * check if pair exists in polymer pairs
        #   * create left and right for new pairs formed by insertion of character
        #   * increment inserted character's element_occurrences count by number of 
        #     times the pair that generates it has been counted
        #     (i.e., if NN appeared 10 times in previous step, and NN -> C, C will be added 10 times)
        #   * increment count of times newly created pairs have appeared
        #     (i.e., count of NC and CN += 1)
        for pair, insertion in rules.items():
            existing_pairs = polymer_pairs.get(pair)
            if existing_pairs is None:
                continue
            left, right = pair[0] + insertion, insertion+pair[1]
            element_occurrences[insertion] = element_occurrences.get(insertion, 0) + existing_pairs

            new_pairs[left] = new_pairs.get(left, 0) + existing_pairs
            new_pairs[right] = new_pairs.get(right, 0) + existing_pairs

        polymer_pairs = new_pairs
    
    return polymer_pairs, element_occurrences


polymer_pairs, element_occurrences = process(template, rules, 40)

most_common = max(element_occurrences, key=element_occurrences.get)
least_common = min(element_occurrences, key=element_occurrences.get)
print(f"most_common: {element_occurrences[most_common]}")
print(f"least_common: {element_occurrences[least_common]}")
print(element_occurrences[most_common] - element_occurrences[least_common])