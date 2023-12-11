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
def pos_in_range(coord):
    return coord[0] >= 0 and coord[0] < len(pipe_map) and coord[1] >= 0 and coord[1] < len(pipe_map[0])
while bfs_queue:
    new_pos = bfs_queue.popleft()
    pipe_symbol = pipe_map[new_pos[0]][new_pos[1]]
    filled_neighbour_count = 0
    max_neighbour_dist = 0
    for i, delta in enumerate(dir_deltas):
        if pipe_symbol in connections[i]:
            neighbour_pos = new_pos[0] + delta[0], new_pos[1] + delta[1]
            if pos_in_range(neighbour_pos):
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
        print(max_neighbour_dist)
        exit(0)
