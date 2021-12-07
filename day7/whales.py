import json
file = open('input.txt', 'r')
input = file.read().splitlines()[0].split(',')

min = int(min(input))
max = int(max(input))

### part 1

fuel_costs = {_: 0 for _ in range(min, max+1)}

for i in range(min, max+1):
    total_fuel_cost = 0
    for position in input:
        distance = abs(int(position) - i)
        total_fuel_cost += distance
    fuel_costs[i] = total_fuel_cost

min = fuel_costs[0]
for e in fuel_costs:
    if fuel_costs[e] < min:
        min = fuel_costs[e]

print(json.dumps(fuel_costs))
print(min)


### part 2

def get_fuel_cost(distance):
    i = distance
    ret = 0
    while i > 0:
        ret += i
        i-=1
    return ret
    

for i in range(min, max+1):
    total_fuel_cost = 0
    for position in input:
        distance = abs(int(position) -i)
        total_fuel_cost += get_fuel_cost(distance)
    fuel_costs[i] = total_fuel_cost


min = fuel_costs[0]
for e in fuel_costs:
    if fuel_costs[e] < min:
        min = fuel_costs[e]

print(json.dumps(fuel_costs))
print(min)