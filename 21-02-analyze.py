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
deltas = [
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0)
]
print(f"{len(flower_map)}X{len(flower_map[0])}")
for i, row in enumerate(flower_map):
    if not any(c == -1 for c in row):
        print(i)
