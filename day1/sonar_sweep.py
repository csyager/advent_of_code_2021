file = open('input.txt', 'r')
input = file.readlines()

### part 1

increases = 0
for i in range(1, len(input)):
    if int(input[i]) > int(input[i-1]):
        print(f"{input[i-1]} -> {input[i]}")
        increases += 1
print(increases)

### part 2

increases = 0
for i in range(3, len(input)):
    if int(input[i-3]) + int(input[i-2]) + int(input[i-1]) < int(input[i-2]) + int(input[i-1]) + int(input[i]):
        increases += 1

print(increases)