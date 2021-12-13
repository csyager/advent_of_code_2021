
class Cave():
    def __init__(self, name:str, small:bool):
        self.name = name
        self.adjacents = []
        self.small = small
        self.visited = False

file = open('input.txt', 'r')
input_file = file.read().splitlines()

# create caves
caves = {}
for line in input_file:
    name_a = line.split('-')[0]
    name_b = line.split('-')[1]
    if name_a not in caves.keys():
        cave_a = Cave(name_a, name_a.islower())
        caves[name_a] = cave_a
    else:
        cave_a = caves[name_a]
    if name_b not in caves.keys():
        cave_b = Cave(name_b, name_b.islower())
        caves[name_b] = cave_b
    else:
        cave_b = caves[name_b]
    cave_a.adjacents.append(cave_b)
    cave_b.adjacents.append(cave_a)

### part 1

def find_paths(start:Cave, end:Cave, visited, path):
    num_found = 0
    visited[start] = True
    path.append(start)
    if start == end:
        str = []
        for cave in path:
            if cave != end:
                str.append(cave.name + " -> ")
            else:
                str.append(cave.name)
        print(''.join(str))
        num_found += 1
    else:
        for i in start.adjacents:
            if not (i.small and visited[i]):
                num_found += find_paths(i, end, visited, path)
    
    path.pop()
    visited[start] = False
    return num_found

### part 2
def find_paths_v2(start:Cave, end:Cave, visits, path, double_visit_used):
    num_found = 0
    visits[start] += 1
    path.append(start)
    if start == end:
        str = []
        for cave in path:
            if cave != end:
                str.append(cave.name + " -> ")
            else:
                str.append(cave.name)
        print(''.join(str))
        num_found += 1
    else:
        for i in start.adjacents:
            if not (i.small and visits[i] >= 1):
                num_found += find_paths_v2(i, end, visits, path, double_visit_used)
            if not double_visit_used and i.small and visits[i] == 1 and i.name != "start" and i.name != "end":
                num_found += find_paths_v2(i, end, visits, path, True)
    
    path.pop()
    if start.small and double_visit_used and visits[start] == 2:
        double_visit_used = False
    visits[start] -= 1
    return num_found

visited_map = {}
for cave in caves.values():
    visited_map[cave] = False

# print(find_paths(caves['start'], caves['end'], visited_map, []))

visits_map = {}
for cave in caves.values():
    visits_map[cave] = 0

print(find_paths_v2(caves['start'], caves['end'], visits_map, [], False))