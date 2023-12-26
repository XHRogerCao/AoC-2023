from collections import deque
infile = open("input.txt", "r")
flower_map = []
bfs_queue = deque()
for i, line in enumerate(infile.read().strip().split("\n")):
    flower_map.append([])
    for j, c in enumerate(line):
        if c == "S":
            flower_map[-1].append(0)
            bfs_queue.append((i, j))
        elif c == ".":
            flower_map[-1].append(10 ** 10)
        else:
            flower_map[-1].append(-1)
count = 0
deltas = [
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0)
]
STEP_LIMIT = 64
while bfs_queue:
    i, j = bfs_queue.popleft()
    if flower_map[i][j] % 2 == 0:
        count += 1
    if flower_map[i][j] < STEP_LIMIT:
        for di, dj in deltas:
            ni, nj = i + di, j + dj
            if ni >= 0 and ni < len(flower_map) and nj >= 0 and nj < len(flower_map[0]):
                if flower_map[ni][nj] == 10 ** 10:
                    flower_map[ni][nj] = flower_map[i][j] + 1
                    bfs_queue.append((ni, nj))
print(count)
