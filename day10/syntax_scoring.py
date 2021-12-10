import math

file = open('input.txt', 'r')
input_file = file.read().splitlines()

class NoIllegalCharException(Exception):
    def __init__(self, message):
        self.message = message

corrupted_score_map = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

uncorrupted_score_map = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

first_illegal_chars = []

def get_first_illegal_char(line):
    stack = []
    for c in line:
        if c == "(" or c == "[" or c == "{" or c == "<":
            stack.append(c)
        else:
            removed_char = stack.pop()
            if removed_char == "(" and c != ")":
                return c
            if removed_char == "[" and c != "]":
                return c
            if removed_char == "{" and c != "}":
                return c
            if removed_char == "<" and c != ">":
                return c
    raise NoIllegalCharException("No illegal char found")
    
uncorrupted_lines = []
for line in input_file:
    try:
        first_illegal_char = get_first_illegal_char(line)
        first_illegal_chars.append(first_illegal_char)
    except NoIllegalCharException:
        uncorrupted_lines.append(line)

### part 1

corrupted_score = 0
for char in first_illegal_chars:
    corrupted_score += corrupted_score_map[char]

print(corrupted_score)

### part 2

def complete_line(line) -> str:
    stack = []
    for c in line:
        if c == "(" or c == "[" or c == "{" or c == "<":
            stack.append(c)
        if c == ")" or c == "]" or c == "}" or c == ">":
            stack.pop()
    ret = []
    while len(stack) != 0:
        opening_char = stack.pop()
        if opening_char == "(":
            ret.append(")")
        if opening_char == "[":
            ret.append("]")
        if opening_char == "{":
            ret.append("}")
        if opening_char == "<":
            ret.append(">")
    return "".join(ret)

scores = []
for line in uncorrupted_lines:
    suffix = complete_line(line)
    score = 0
    for c in suffix:
        score *= 5
        score += uncorrupted_score_map[c]
    scores.append(score)

scores = sorted(scores, reverse=True)
print(scores[int(len(scores)/2)])