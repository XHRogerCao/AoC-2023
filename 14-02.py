rock_map = []
while True:
    inputval = input()
    if not inputval:
        break
    rock_map.append(list(inputval))
cycle_count = 0
cycle_maps = {}
MAX_COUNT = 1000000000
while cycle_count < MAX_COUNT:
    cycle_count += 1
    for col in range(len(rock_map[0])):
        last_top = 0
        for row in range(len(rock_map)):
            if rock_map[row][col] == "#":
                last_top = row + 1
            elif rock_map[row][col] == "O":
                rock_map[row][col], rock_map[last_top][col] = rock_map[last_top][col], rock_map[row][col]
                last_top += 1
    for row in range(len(rock_map)):
        last_top = 0
        for col in range(len(rock_map[0])):
            if rock_map[row][col] == "#":
                last_top = col + 1
            elif rock_map[row][col] == "O":
                rock_map[row][col], rock_map[row][last_top] = rock_map[row][last_top], rock_map[row][col]
                last_top += 1
    for col in range(len(rock_map[0])):
        last_top = len(rock_map) - 1
        for row in reversed(range(len(rock_map))):
            if rock_map[row][col] == "#":
                last_top = row - 1
            elif rock_map[row][col] == "O":
                rock_map[row][col], rock_map[last_top][col] = rock_map[last_top][col], rock_map[row][col]
                last_top -= 1
    for row in range(len(rock_map)):
        last_top = len(rock_map[0]) - 1
        for col in reversed(range(len(rock_map[0]))):
            if rock_map[row][col] == "#":
                last_top = col - 1
            elif rock_map[row][col] == "O":
                rock_map[row][col], rock_map[row][last_top] = rock_map[row][last_top], rock_map[row][col]
                last_top -= 1
    snapshot = "\n".join("".join(row) for row in rock_map)
    if snapshot in cycle_maps:
        cycle_size = cycle_count - cycle_maps[snapshot]
        print(f"Current Cycle: {cycle_count}; size: {cycle_size}")
        cycle_count += (MAX_COUNT - cycle_count) // cycle_size * cycle_size
    cycle_maps[snapshot] = cycle_count
total = 0
for i, row in enumerate(rock_map):
    for c in row:
        if c == "O":
            total += len(rock_map) - i
print(total)
