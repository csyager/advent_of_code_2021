file = open('input.txt', 'r')
input_file = file.read().splitlines()

class Point():
    def __init__(self, line, col, value: int):
        self.line = line
        self.col = col
        self.value = value
        self.visited = False

grid = []
for line_num in range(len(input_file)):
    line = input_file[line_num]
    l = []
    for col_num in range(len(line)):
        c = input_file[line_num][col_num]
        l.append(Point(line_num, col_num, int(c)))
    grid.append(l)

low_points = []

### part 1

def find_adjacents(line, col) -> list[Point]:
    adjacents = []
    if line != 0:
        # top middle
        adjacents.append(grid[line-1][col])
    if col != 0:
        # left
        adjacents.append(grid[line][col-1])
    if col != len(grid[0]) -1:
        # right
        adjacents.append(grid[line][col+1])
    if line != len(grid) -1:
        # bottom center
        adjacents.append(grid[line+1][col])
    
    return adjacents

for line in range(len(grid)):
    for col in range(len(grid[0])):
        adjacents = find_adjacents(line, col)
    
        low_point = True
        for elem in adjacents:
            if grid[line][col].value > elem.value:
                low_point = False
        if low_point:
            low_points.append(grid[line][col])

sum = 0
for point in low_points:
    sum += 1 + point.value

print(sum)

def get_basin_size(line, col) -> int:
    current_point = grid[line][col]
    current_point.visited = True
    adjacents = find_adjacents(line, col)
    size = 1
    for point in adjacents:
        if point.value != 9 and point.visited == False:
            size += get_basin_size(point.line, point.col)
            print(size)
    return size

basin_sizes = []
for point in low_points:
    basin_sizes.append(get_basin_size(point.line, point.col))

basin_sizes = sorted(basin_sizes, reverse=True)
print(basin_sizes[0] * basin_sizes[1] * basin_sizes[2])