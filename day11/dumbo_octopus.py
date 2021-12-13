class Octopus():
    def __init__(self, energy:int):
        self.energy = energy
        self.adjacents = []
        self.flashes = 0
    
    def set_adjacents(self, adjacents):
        self.adjacents = adjacents

    def increment_energy(self):
        self.energy += 1

    def try_flash(self, has_flashed):
        if self.energy > 9 and self not in has_flashed:
            has_flashed.append(self)
            self.flashes += 1
            for octopus in self.adjacents:
                octopus.increment_energy()
                octopus.try_flash(has_flashed)

file = open('input.txt', 'r')
input_file = file.read().splitlines()

grid = []

# build grid
for line in input_file:
    l = []
    for c in line:
        o = Octopus(int(c))
        l.append(o)
    grid.append(l)

def get_adjacents(grid, row, col):
    adjacents = []
    if row != 0:
        # top
        if col != 0:
            # top left
            adjacents.append(grid[row-1][col-1])
        adjacents.append(grid[row-1][col])
        if col != len(grid[0])-1:
            adjacents.append(grid[row-1][col+1])
    if col != 0:
        adjacents.append(grid[row][col-1])
    if col != len(grid[0])-1:
        adjacents.append(grid[row][col+1])
    if row != len(grid)-1:
        # bottom
        if col != 0:
            adjacents.append(grid[row+1][col-1])
        adjacents.append(grid[row+1][col])
        if col != len(grid[0])-1:
            adjacents.append(grid[row+1][col+1])
    return adjacents

# set adjacents for each octopus
for row_num in range(len(grid)):
    row = grid[row_num]
    for col_num in range(len(row)):
        octopus = grid[row_num][col_num]
        octopus.set_adjacents(get_adjacents(grid, row_num, col_num))

def step(grid: list, step_num: int) -> list:
    has_flashed = []
    for row_num in range(len(grid)):
        row = grid[row_num]
        for col_num in range(len(row)):
            octopus:Octopus = grid[row_num][col_num]
            octopus.increment_energy()

    for row_num in range(len(grid)):
        row = grid[row_num]
        for col_num in range(len(row)):
            octopus = grid[row_num][col_num]
            octopus.try_flash(has_flashed)

    for octopus in has_flashed:
        octopus.energy = 0
    
    return has_flashed
    
flashed_simultaneously = False
step_num = 1
while not flashed_simultaneously:
    has_flashed = step(grid, step_num)
    if len(has_flashed) == len(grid) * len(grid[0]):
        flashed_simultaneously = True
        print(f"flashed simultaneously on step {step_num}")
    step_num += 1

num_flashes = 0
for row_num in range(len(grid)):
    row = grid[row_num]
    for col_num in range(len(row)):
        num_flashes += grid[row_num][col_num].flashes

print(num_flashes)