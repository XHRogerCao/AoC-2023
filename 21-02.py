from collections import deque
from math import ceil
infile = open("input.txt", "r")
flower_map = []
for i in range(9):
    flower_map.append([])
starting_pos = None
for i, line in enumerate(infile.read().strip().split("\n")):
    for k in range(9):
        flower_map[k].append([])
    for j, c in enumerate(line):
        if c == "S":
            for k in range(9):
                flower_map[k][-1].append(10 ** 10)
            starting_pos = (i, j)
        elif c == ".":
            for k in range(9):
                flower_map[k][-1].append(10 ** 10)
        else:
            for k in range(9):
                flower_map[k][-1].append(-1)
parity_count = [0, 0]
deltas = [
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0)
]
STEP_LIMIT = 26501365
print(f"{len(flower_map[0])}X{len(flower_map[0][0])}")
max_dists = [0] * 9
for start_i, row_idx in enumerate([0, starting_pos[0], len(flower_map[0]) - 1]):
    for start_j, col_idx in enumerate([0, starting_pos[1], len(flower_map[0][0]) - 1]):
        flower_idx = start_i * 3 + start_j
        bfs_queue = deque()
        bfs_queue.append((row_idx, col_idx))
        flower_map[flower_idx][row_idx][col_idx] = 0
        while bfs_queue:
            i, j = bfs_queue.popleft()
            if flower_idx == 4:
                parity_count[flower_map[flower_idx][i][j] % 2] += 1
            max_dists[flower_idx] = max(max_dists[flower_idx], flower_map[flower_idx][i][j])
            for di, dj in deltas:
                ni, nj = i + di, j + dj
                if ni >= 0 and ni < len(flower_map[flower_idx]) and nj >= 0 and nj < len(flower_map[flower_idx][0]):
                    if flower_map[flower_idx][ni][nj] == 10 ** 10:
                        flower_map[flower_idx][ni][nj] = flower_map[flower_idx][i][j] + 1
                        bfs_queue.append((ni, nj))
# for one_map in flower_map:
#     for row in one_map:
#         for col in row:
#             if col == 10 ** 10:
#                 print(".", end="\t")
#             elif col == -1:
#                 print("#", end="\t")
#             else:
#                 print(col, end="\t")
#         print("")
#     print("")
print(max_dists)
count = 0
max_orth_dist = max(max_dists[1], max_dists[3], max_dists[5], max_dists[7])
# Number of blocks orthogonally completely full. It forms a diamond shape, which we can use to calculate
max_orth_full = ceil((STEP_LIMIT - (len(flower_map[0]) // 2 + 1) - max_orth_dist) / len(flower_map[0]))
print(max_orth_full)
count += parity_count[STEP_LIMIT % 2] * ((2 * (max_orth_full // 2) + 1) ** 2)
print(f"{parity_count[STEP_LIMIT % 2]} X {((2 * (max_orth_full // 2) + 1) ** 2)}")
count += parity_count[(STEP_LIMIT + 1) % 2] * ((2 * ((max_orth_full + 1) // 2)) ** 2)
print(f"{parity_count[(STEP_LIMIT + 1) % 2]} X {((2 * ((max_orth_full + 1) // 2)) ** 2)}")
# Add orthogonal entries that doesn't fill fully
for i in range(1, 9, 2):
    current_dist = (len(flower_map[0]) // 2 + 1) + max_orth_full * len(flower_map[0])
    while current_dist <= STEP_LIMIT:
        local_count = 0
        for j, row in enumerate(flower_map[i]):
            for k, d in enumerate(row):
                if d != -1 and current_dist + d <= STEP_LIMIT and (current_dist + d) % 2 == STEP_LIMIT % 2:
                    local_count += 1
        count += local_count
        print(f"{local_count} X {1}")
        current_dist += len(flower_map[0])
for i in range(0, 9, 2):
    if i == 4:
        continue
    current_dist = 2 * (len(flower_map[0]) // 2 + 1) + (max_orth_full - 1) * len(flower_map[0])
    cell_count = max_orth_full
    while current_dist <= STEP_LIMIT:
        local_count = 0
        for j, row in enumerate(flower_map[i]):
            for k, d in enumerate(row):
                if d != -1 and current_dist + d <= STEP_LIMIT and (current_dist + d) % 2 == STEP_LIMIT % 2:
                    local_count += 1
        count += local_count * cell_count
        current_dist += len(flower_map[0])
        print(f"{local_count} X {cell_count}")
        cell_count += 1
print(count)
