file = open('input.txt', 'r')
input_file = file.read().splitlines()

inputs = []
outputs = []

for line in input_file:
    inputs.append(line.split(' | ')[0])
    outputs.append(line.split(' | ')[1])

unique_segments_to_digit = {
    2: 1,
    4: 4,
    3: 7,
    7: 8
}

### part 1

count_unique_digit_outputs = 0
for line in outputs:
    for s in line.split():
        if len(s) in unique_segments_to_digit.keys():
            count_unique_digit_outputs += 1

print(count_unique_digit_outputs)


### part 2

#  aaaa
# b    c
# b    c
#  dddd
# e    f
# e    f
#  gggg

segments = {
    'a': '',
    'b': '',
    'c': '',
    'd': '',
    'e': '',
    'f': '',
    'g': ''
}

# for testing:
inputs = inputs[:1]

for line in inputs:

    digit_to_input = {
        0: '',
        1: '',
        2: '',
        3: '',
        4: '',
        5: '',
        6: '',
        7: '',
        8: '',
        9: ''
    }
    for s in line.split():
        if len(s) in unique_segments_to_digit.keys():
            if digit_to_input[unique_segments_to_digit[len(s)]] == '':
                digit_to_input[unique_segments_to_digit[len(s)]] = s

    # 7 = 1 + segment a
    for c in digit_to_input[7]:
        if c not in digit_to_input[1]:
            segments['a'] = c
        
    # 2 and 3 are both 5 segments with only one difference, 5 is the leftover
    five_segments = []
    for s in line.split():
        if len(s) == 5 and ''.join(sorted(s)) not in five_segments:
            five_segments.append(''.join(sorted(s)))

    for elem in five_segments:
        for elem2 in five_segments:
            if elem != elem2 and segments['f'] == '' and segments['e'] == '':
                count = sum(1 for a, b in zip(elem, elem2) if a != b)
                if count == 1:
                    # 2 and 3
                    for c in elem:
                        if c not in elem2:
                            if c in digit_to_input[4]:
                                segments['f'] = c
                                digit_to_input[3] = elem
                                digit_to_input[2] = elem2
                            else:
                                segments['e'] = c
                                digit_to_input[2] = elem
                                digit_to_input[3] = elem2
                    for c in elem2:
                        if c not in elem:
                            if segments['f'] == '':
                                segments['f'] = c
                            else:
                                segments['e'] = c

    for elem in five_segments:
        if elem not in digit_to_input.values():
            digit_to_input[5] = elem
            for c in elem:
                if c not in digit_to_input[3]:
                    segments['b'] = c
    
    for c in digit_to_input[4]:
        if c not in digit_to_input[1] and c not in digit_to_input[2]:
            segments['b'] = c
        
    for c in digit_to_input[1]:
        if c not in digit_to_input[5]:
            segments['c'] = c

    for c in digit_to_input[2]:
        if c in digit_to_input[4] and c != segments['c']:
            segments['d'] = c

    print(segments)
    print(digit_to_input)