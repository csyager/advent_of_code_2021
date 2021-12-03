import json

file = open('input.txt', 'r')
input = file.readlines()

### part 1

map = {}
for i in range(12):
    map[str(i)] = {'0': 0, '1': 0}
for line in input:
    for i in range(12):
        map[str(i)][line[i]] += 1

gamma_binary_string = ""
for position in map.keys():
    if map[position]['1'] > map[position]['0']:
        gamma_binary_string += "1"
    else:
        gamma_binary_string += "0"
    

gamma = int(gamma_binary_string, base=2)

epsilon_binary_string = ""
for c in gamma_binary_string:
    if c == '0':
        epsilon_binary_string += "1"
    else:
        epsilon_binary_string += "0"

epsilon = int(epsilon_binary_string, base=2)

print(gamma * epsilon)

### part 2
oxygen_list = input.copy()
while(len(oxygen_list) > 1):
    for position in range(0, 12):
        new_oxygen_list = []
        ones = 0
        zeroes = 0
        for elem in oxygen_list:
            if elem[int(position)] == '1':
                ones += 1
            else:
                zeroes += 1
            
        if ones >= zeroes:
            for line_number in range(len(oxygen_list)):
                if oxygen_list[line_number][int(position)] == '1':
                    new_oxygen_list.append(oxygen_list[line_number])
        else:
            for line_number in range(len(oxygen_list)):
                if oxygen_list[line_number][int(position)] == '0':
                    new_oxygen_list.append(oxygen_list[line_number])
        oxygen_list = new_oxygen_list
        if len(oxygen_list) == 1:
            break

print(oxygen_list)

co2_list = input.copy()

while(len(co2_list) > 1):
    for position in map.keys():
        new_co2_list = []
        ones = 0
        zeroes = 0
        for elem in co2_list:
            if elem[int(position)] == '1':
                ones += 1
            else:
                zeroes += 1

        if zeroes <= ones:
            for line_number in range(len(co2_list)):
                if co2_list[line_number][int(position)] == '0':
                    new_co2_list.append(co2_list[line_number])
        else:
            for line_number in range(len(co2_list)):
                if co2_list[line_number][int(position)] == '1':
                    new_co2_list.append(co2_list[line_number])
        co2_list = new_co2_list
        if len(co2_list) == 1:
            break

oxygen_value = int(oxygen_list[0], base=2)
co2_value = int(co2_list[0], base=2)
print(oxygen_value)
print(co2_value)

print(oxygen_value * co2_value)
