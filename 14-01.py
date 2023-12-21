rock_map = []
while True:
    inputval = input()
    if not inputval:
        break
    rock_map.append(list(inputval))
for col in range(len(rock_map[0])):
    last_top = 0
    for row in range(len(rock_map)):
        if rock_map[row][col] == "#":
            last_top = row + 1
        elif rock_map[row][col] == "O":
            rock_map[row][col], rock_map[last_top][col] = rock_map[last_top][col], rock_map[row][col]
            last_top += 1
total = 0
for i, row in enumerate(rock_map):
    for c in row:
        if c == "O":
            total += len(rock_map) - i
print(total)
