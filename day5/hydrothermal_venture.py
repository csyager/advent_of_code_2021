file = open('input.txt', 'r')
input = file.read().splitlines()

class Line():
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

class Grid():
    def __init__(self, length, width):
        self.length = length
        self.width = width
        plot = []
        for i in range(length):
            row = []
            for j in range(width):
                row.append('.')
            plot.append(row)
            self.plot = plot

    def __str__(self):
        string_builder = []
        for y in range(self.length):
            for x in range(self.width):
                string_builder.append(self.plot[y][x])
            string_builder.append('\n')
        return ''.join(string_builder)

    def plot_point(self, x, y):
        if self.plot[y][x] == '.':
            self.plot[y][x] = '1'
        else:
            self.plot[y][x] = str(int(self.plot[y][x]) + 1)

    def plot_horizontal_line(self, y, x1, x2):
        if (x1 < x2):
            for x in range(x1, x2 + 1):
                self.plot_point(x, y)
        else:
            for x in range(x2, x1 + 1):
                self.plot_point(x, y)

    def plot_vertical_line(self, x, y1, y2):
        if y1 < y2:
            for y in range(y1, y2 + 1):
                self.plot_point(x, y)
        else:
            for y in range(y2, y1 + 1):
                self.plot_point(x, y)

    def plot_diagonal_line(self, x1, x2, y1, y2):
        cur_x = x1
        cur_y = y1
        if x1 < x2:
            if y1 < y2:
                # down and right
                while cur_x <= x2 and cur_y <= y2:
                    self.plot_point(cur_x, cur_y)
                    cur_x += 1
                    cur_y += 1
            else:
                # up and right
                while cur_x <= x2 and cur_y >=y2:
                    self.plot_point(cur_x, cur_y)
                    cur_x += 1
                    cur_y -= 1
            
        else:
            if y1 < y2:
                # down and left
                while cur_x >= x2 and cur_y <= y2:
                    self.plot_point(cur_x, cur_y)
                    cur_x -= 1
                    cur_y += 1        
            else:
                # up and left
                while cur_x >= x2 and cur_y >= y2:
                    self.plot_point(cur_x, cur_y)
                    cur_x -= 1
                    cur_y -= 1

        
    def plot_line(self, l: Line):
        if l.y1 == l.y2:
            y = l.y1
            self.plot_horizontal_line(y, l.x1, l.x2)
        
        elif l.x1 == l.x2:
            x = l.x1
            self.plot_vertical_line(x, l.y1, l.y2)

        else:
            self.plot_diagonal_line(l.x1, l.x2, l.y1, l.y2)
        

    def count_two_or_more(self):
        count = 0
        for y in range(self.length):
            for x in range(self.width):
                if self.plot[y][x] != '.':
                    if int(self.plot[y][x]) >= 2:
                        count += 1
        return count

grid = Grid(1000, 1000)
for line in input:
    points = line.split()
    point_1 = points[0]
    point_2 = points[2]
    x1 = int(point_1.split(',')[0])
    y1 = int(point_1.split(',')[1])
    x2 = int(point_2.split(',')[0])
    y2 = int(point_2.split(',')[1])
    l = Line(x1, y1, x2, y2)
    grid.plot_line(l)
print(grid)
print(grid.count_two_or_more())