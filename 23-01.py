infile = open("input.txt", "r")
snow_map = infile.read().strip().split("\n")
travelled = set()
max_dist = 0
deltas = [
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0)
]
dirs = [">", "v", "<", "^"]
move_stack = [[0, 0, snow_map[0].find(".")]]
travelled.add((0, snow_map[0].find(".")))
def pop_top():
    travelled.remove((move_stack[-1][1], move_stack[-1][2]))
    move_stack.pop()
    if move_stack:
        move_stack[-1][0] += 1
while move_stack:
    i, row, col = move_stack[-1]
    if row == len(snow_map) - 1:
        max_dist = max(max_dist, len(move_stack) - 1)
        pop_top()
    elif i == 4:
        pop_top()
    else:
        n_row, n_col = row + deltas[i][0], col + deltas[i][1]
        if n_row >= 0 and n_row < len(snow_map) and n_col >= 0 and n_col < len(snow_map[0]) and (snow_map[n_row][n_col] == "." or snow_map[n_row][n_col] == dirs[i]) and ((n_row, n_col) not in travelled):
            # Can add
            travelled.add((n_row, n_col))
            move_stack.append([0, n_row, n_col])
        else:
            move_stack[-1][0] += 1
print(max_dist)
