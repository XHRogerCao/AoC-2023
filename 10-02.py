pipe_map = []
starting_pos = (0, 0)
while True:
    inputval = input()
    if not inputval:
        break
    idx = inputval.find("S")
    if idx != -1:
        starting_pos = (len(pipe_map), idx)
    pipe_map.append(inputval)
connections = [
    ["S", "-", "F", "L"],
    ["S", "|", "F", "7"],
    ["S", "-", "J", "7"],
    ["S", "|", "L", "J"]
]
dir_deltas = [
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0)
]
from collections import deque

dist_map = []
for row in pipe_map:
    dist_map.append([])
    for c in row:
        if c == "S":
            dist_map[-1].append(0)
        else:
            dist_map[-1].append(-1)

bfs_queue = deque()
bfs_queue.append(starting_pos)
def pos_in_range(coord, map_to_check):
    return coord[0] >= 0 and coord[0] < len(map_to_check) and coord[1] >= 0 and coord[1] < len(map_to_check[0])
cycle_point = (0, 0)
while bfs_queue:
    new_pos = bfs_queue.popleft()
    pipe_symbol = pipe_map[new_pos[0]][new_pos[1]]
    filled_neighbour_count = 0
    max_neighbour_dist = 0
    for i, delta in enumerate(dir_deltas):
        if pipe_symbol in connections[i]:
            neighbour_pos = new_pos[0] + delta[0], new_pos[1] + delta[1]
            if pos_in_range(neighbour_pos, pipe_map):
                neighbour_symbol = pipe_map[neighbour_pos[0]][neighbour_pos[1]]
                if neighbour_symbol in connections[(i + 2) % 4]:
                    # Connection established
                    if dist_map[neighbour_pos[0]][neighbour_pos[1]] == -1:
                        dist_map[neighbour_pos[0]][neighbour_pos[1]] = dist_map[new_pos[0]][new_pos[1]] + 1
                        bfs_queue.append(neighbour_pos)
                    else:
                        filled_neighbour_count += 1
                        max_neighbour_dist = max(max_neighbour_dist, dist_map[neighbour_pos[0]][neighbour_pos[1]])
    # print(dist_map)
    if filled_neighbour_count == 2:
        cycle_point = new_pos
        break
loop_find_queue = deque()
loop_find_queue.append(cycle_point)
# Triple up the flood map to mark the walls
flood_map = []
for i, row in enumerate(pipe_map):
    flood_map.append([])
    flood_map.append([])
    flood_map.append([])
    for j, c in enumerate(row):
        if (i, j) == cycle_point:
            flood_map[-1].append(0)
            flood_map[-2].append(0)
            flood_map[-3].append(0)
            flood_map[-1].append(0)
            flood_map[-2].append(1)
            flood_map[-3].append(0)
            flood_map[-1].append(0)
            flood_map[-2].append(0)
            flood_map[-3].append(0)
        else:
            flood_map[-1].append(0)
            flood_map[-2].append(0)
            flood_map[-3].append(0)
            flood_map[-1].append(0)
            flood_map[-2].append(0)
            flood_map[-3].append(0)
            flood_map[-1].append(0)
            flood_map[-2].append(0)
            flood_map[-3].append(0)
# Wall off the cycle
while loop_find_queue:
    new_pos = loop_find_queue.popleft()
    pipe_symbol = pipe_map[new_pos[0]][new_pos[1]]
    filled_neighbour_count = 0
    max_neighbour_dist = 0
    for i, delta in enumerate(dir_deltas):
        if pipe_symbol in connections[i]:
            flood_map[new_pos[0] * 3 + 1 + delta[0]][new_pos[1] * 3 + 1 + delta[1]] = 1
    if pipe_symbol == "S":
        continue
    for i, delta in enumerate(dir_deltas):
        if pipe_symbol in connections[i]:
            neighbour_pos = new_pos[0] + delta[0], new_pos[1] + delta[1]
            if pos_in_range(neighbour_pos, pipe_map):
                neighbour_symbol = pipe_map[neighbour_pos[0]][neighbour_pos[1]]
                if neighbour_symbol in connections[(i + 2) % 4]:
                    # Connection established
                    if flood_map[neighbour_pos[0] * 3 + 1][neighbour_pos[1] * 3 + 1] == 0:
                        flood_map[neighbour_pos[0] * 3 + 1][neighbour_pos[1] * 3 + 1] = 1
                        loop_find_queue.append(neighbour_pos)
                    else:
                        filled_neighbour_count += 1
                        max_neighbour_dist = max(max_neighbour_dist, dist_map[neighbour_pos[0]][neighbour_pos[1]])
# Flood the map starting from the edge
flood_queue = deque()
for i in range(len(flood_map)):
    if flood_map[i][0] == 0:
        flood_map[i][0] = -1
        flood_queue.append((i, 0))
    if flood_map[i][-1] == 0:
        flood_map[i][-1] = -1
        flood_queue.append((i, len(flood_map[0]) - 1))
for j in range(len(flood_map[0])):
    if flood_map[0][j] == 0:
        flood_map[0][j] = -1
        flood_queue.append((0, j))
    if flood_map[-1][j] == 0:
        flood_map[-1][j] = -1
        flood_queue.append((len(flood_map) - 1, j))
while flood_queue:
    new_pos = flood_queue.popleft()
    for i, delta in enumerate(dir_deltas):
        neighbour_pos = new_pos[0] + delta[0], new_pos[1] + delta[1]
        if pos_in_range(neighbour_pos, flood_map) and flood_map[neighbour_pos[0]][neighbour_pos[1]] == 0:
            flood_map[neighbour_pos[0]][neighbour_pos[1]] = -1
            flood_queue.append(neighbour_pos)
total = 0
# for i, row in enumerate(flood_map):
#     for j, col in enumerate(row):
#         if col == 0:
#             print(".", end="")
#         elif col == -1:
#             print("~", end="")
#         else:
#             print("#", end="")
#         if j % 3 == 2:
#             print(" ", end="")
#     print("")
#     if i % 3 == 2:
#         print("")
for i in range(0, len(flood_map), 3):
    for j in range(0, len(flood_map[0]), 3):
        any_filled = False
        for k in range(3):
            for l in range(3):
                if flood_map[i + k][j + l] != 0:
                    any_filled = True
        if not any_filled:
            total += 1
print(total)
