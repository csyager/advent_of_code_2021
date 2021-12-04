file = open('input.txt', 'r')
input = file.read().splitlines()

class Board():
    def __init__(self, rows: list):
        self.rows = rows
        self.won = False
    
    def has_won(self, nums: list):
        # check rows
        # for row in self.rows:
        for row in self.rows:
            won_rowwise = True
            for value in row.split():
                value = int(value)
                if value not in nums:
                    won_rowwise = False
            if won_rowwise:
                print("won rowwise " + str(row.split()))
                return True

        # check cols:
        for col_num in range(5):
            won_colwise = True
            for row in self.rows:
                row = row.split()
                value = int(row[col_num])
                if value not in nums:
                    won_colwise = False
            if won_colwise:
                col = []
                for row in self.rows:
                    row = row.split()
                    col.append(int(row[col_num]))
                print("won colwise " + str(col))
                return True
        
        return False
    
    def calculate_score(self, nums:list):
        nums_on_board = []
        for row in self.rows:
            for value in row.split():
                value = int(value)
                nums_on_board.append(value)
        for num in nums:
            if num in nums_on_board:
                nums_on_board.remove(num)
        sum = 0
        for num in nums_on_board:
            sum += num
        return sum

    def __str__(self):
        return str(self.rows)
        

### part 1

numbers = input[0].split(',')
line_num = 2
boards = []

while line_num < len(input):
    board = input[line_num:line_num + 5]
    b = Board(board)
    boards.append(b)
    line_num += 6

called_numbers = []
winner_found = False
for number in numbers:
    called_numbers.append(number)
    for board in boards:
        if board.has_won(called_numbers) and not winner_found:
            winner_found = True
            print(board)
            print(number)
            print(called_numbers)
            print(board.calculate_score(called_numbers) * int(number))


### part 2
called_numbers = []
remaining_boards = boards.copy()
for number in numbers:
    called_numbers.append(int(number))
    for board in remaining_boards:
        if board.has_won(called_numbers):
            remaining_boards.remove(board)
            if len(remaining_boards) == 0:
                # last board removed
                print(board)
                print(number)
                score = board.calculate_score(called_numbers)
                print(score)
                print(score * int(number))

