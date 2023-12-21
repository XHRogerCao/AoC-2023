from collections import deque

deltas = [
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0)
]
mirrors = {
    "/": [[3], [2], [1], [0]],
    "\\": [[1], [0], [3], [2]],
    "-": [[0], [0, 2], [2], [0, 2]],
    "|": [[1, 3], [1], [1, 3], [3]],
}

infile = open("input.txt", "r")
mirror_map = []
for line in infile.read().strip().split("\n"):
    mirror_map.append(line)
best = 0
starting_pos = []
for i in range(len(mirror_map)):
    starting_pos.append((i, -1, 0))
    starting_pos.append((i, len(mirror_map[0]), 2))
for i in range(len(mirror_map[0])):
    starting_pos.append((-1, i, 1))
    starting_pos.append((len(mirror_map), i, 3))
for one_start in starting_pos:
    passed = []
    for line in mirror_map:
        passed.append([])
        for i in range(len(line)):
            passed[-1].append([False, False, False, False])
    beams = deque()
    beams.append(one_start)
    while beams:
        brow, bcol, d = beams.popleft()
        nrow, ncol = brow + deltas[d][0], bcol + deltas[d][1]
        if ncol >= 0 and ncol < len(mirror_map[0]) and nrow >= 0 and nrow < len(mirror_map):
            if not passed[nrow][ncol][d]:
                passed[nrow][ncol][d] = True
                c = mirror_map[nrow][ncol]
                newd = [d]
                if c in mirrors:
                    newd = mirrors[c][d]
                for one_d in newd:
                    beams.append((nrow, ncol, one_d))
    total = 0
    for row in passed:
        for col in row:
            if any(col):
                total += 1
    best = max(total, best)
print(best)
