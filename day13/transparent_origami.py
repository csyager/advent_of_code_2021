file = open('input.txt', 'r')
input_file = file.read().splitlines()

class Grid():
    def __init__(self):
        self.grid = []
        self.points = []
        self.x_len = 0
        self.y_len = 0

    def plot_point(self, x, y):
        while x > self.x_len:
            for line in self.grid:
                line.append('.')
            self.x_len += 1
        while y > self.y_len - 1:
            self.grid.append(['.'] * (self.x_len + 1))
            self.y_len += 1
        if (x, y) not in self.points:
            self.grid[y][x] = "#"
            self.points.append((x, y))
        else: 
            print(f"({x}, {y}) already in grid")

    def fold_x(self, col_num):
        # fold to left
        for point in self.points:
            if point[0] > col_num:
                new_col_num = 2*col_num - point[0]
                self.plot_point(new_col_num, point[1])
                print(f"moving ({point[0]}, {point[1]}) to ({new_col_num}, {point[1]})")
        new_grid = []
        for line in self.grid:
            new_grid.append(line[0:col_num + 1])
        self.grid = new_grid
        self.x_len = len(self.grid[0])
        points_to_remove = []
        for point in self.points:
            if point[0] > col_num:
                points_to_remove.append(point)
        for point in points_to_remove:
            self.points.remove(point)


    def fold_y(self, row_num):
        # fold bottom up
        for point in self.points:
            if point[1] > row_num:
                new_row_num = 2 * row_num - point[1]
                self.plot_point(point[0], new_row_num)
                print(f"moving ({point[0]}, {point[1]}) to ({point[0]}, {new_row_num})")
        self.grid = self.grid[0:row_num + 1]
        self.y_len = len(self.grid)
        points_to_remove = []
        for point in self.points:
            if point[1] > row_num:
                points_to_remove.append(point)
        for point in points_to_remove:
            self.points.remove(point)

    def print_grid(self):
        for line in self.grid:
            print(str(line))

grid = Grid()
instructions = []

for line in input_file:
    if line != "" and line[0].isnumeric():
        x = int(line.split(',')[0])
        y = int(line.split(',')[1])
        grid.plot_point(x, y)
    elif line != "":
        instructions.append(line)

print(f"num points: {len(grid.points)}")

for line in instructions:
    instruction = line.split()[2]
    if instruction[0] == "x":
        
        # vertical fold
        col_num = int(instruction[2:])
        print(f"vertical fold on {int(instruction[2:])}")
        grid.fold_x(col_num)
        print("points: " + str(grid.points))

    else:
        # horizontal fold
        row_num = int(instruction[2:])
        print(f"horizontal fold on {int(row_num)}")
        grid.fold_y(row_num)
        print("points: " + str(grid.points))


grid.print_grid()
