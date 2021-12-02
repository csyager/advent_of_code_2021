file = open('input.txt', 'r')
input = file.readlines()

### part 1

depth = 0
position = 0

for s in input:
    command = s.split()[0]
    unit = s.split()[1]
    if command == "forward":
        position += int(unit)
    elif command == "down":
        depth += int(unit)
    elif command == "up":
        depth -= int(unit)

print(f"depth: {depth}")
print(f"position: {position}")
print(depth * position)

### part 2

depth = 0
position = 0
aim = 0
for s in input:
    command = s.split()[0]
    unit = s.split()[1]
    if command == "forward":
        position += int(unit)
        depth += int(unit) * aim
    elif command == "down":
        aim += int(unit)
    elif command == "up":
        aim -= int(unit)

print(f"depth: {depth}")
print(f"position: {position}")
print(depth * position)