from collections import deque
infile = open("input.txt", "r")
flower_map = []
bfs_queue = deque()
starting_pos = None
for i, line in enumerate(infile.read().strip().split("\n")):
    flower_map.append([])
    for j, c in enumerate(line):
        if c == "S":
            flower_map[-1].append(10 ** 10)
            starting_pos = (i, j)
        elif c == ".":
            flower_map[-1].append(10 ** 10)
        else:
            flower_map[-1].append(-1)
flower_map, old_map = [], flower_map
CELLS = 11
for i in range(CELLS):
    for row in old_map:
        flower_map.append([])
        for j in range(CELLS):
            for col in row:
                flower_map[-1].append(col)
bfs_queue.append((len(old_map) * (CELLS // 2) + starting_pos[0], len(old_map) * (CELLS // 2) + starting_pos[1]))
flower_map[len(old_map) * (CELLS // 2) + starting_pos[0]][len(old_map) * (CELLS // 2) + starting_pos[1]] = 0
count = 0
region_count = []
for i in range(CELLS):
    region_count.append([0] * CELLS)
deltas = [
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0)
]
STEP_LIMIT = 600
while bfs_queue:
    i, j = bfs_queue.popleft()
    if flower_map[i][j] % 2 == 0:
        count += 1
        region_count[i // len(old_map)][j // len(old_map)] += 1
    if flower_map[i][j] < STEP_LIMIT:
        for di, dj in deltas:
            ni, nj = i + di, j + dj
            if ni >= 0 and ni < len(flower_map) and nj >= 0 and nj < len(flower_map[0]):
                if flower_map[ni][nj] == 10 ** 10:
                    flower_map[ni][nj] = flower_map[i][j] + 1
                    bfs_queue.append((ni, nj))
print(count)
for row in region_count:
    for col in row:
        print(col, end="\t")
    print("")
