file = open('input.txt', 'r')
input = file.read().splitlines()[0].split(',')

class Lanternfish():
    def __init__(self, timer: int = 8):
        self.timer = timer

    def __str__(self):
        return str(self.timer)

    def age_one_day(self) -> bool:
        # return true if a new lanternfish should be created
        if self.timer == 0:
            self.timer = 6
            return True
        else:
            self.timer -= 1
            return False

### part 1

lanternfish = []
for i in input:
    lanternfish.append(Lanternfish(int(i)))

for i in range(256):
    new_lanternfish = []
    for l in lanternfish:
        should_create_new = l.age_one_day()
        if should_create_new:
            new_lanternfish.append(Lanternfish())
    for l in new_lanternfish:
        lanternfish.append(l)

for e in lanternfish:
    print(e, end=",")
print()
print(len(lanternfish))

### part 2
# track number of fish of each age instead of fish individually

ages = {i: 0 for i in range(9)}

for i in input:
    ages[int(i)] += 1

for i in range(256):
    new_ages = {_: 0 for _ in range(9)}
    for age in ages:
        if age == 0:
            new_ages[6] = ages[0]
            new_ages[8] = ages[0]
        else:
            new_ages[age-1] += ages[age]

    ages = new_ages

print(sum(ages.values()))