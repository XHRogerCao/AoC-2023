from collections import deque
infile = open("input.txt", "r")
lagoon_map = {(0, 0): 1}
cur_pos = (0, 0)
deltas = {
    "R": (0, 1),
    "L": (0, -1),
    "U": (-1, 0),
    "D": (1, 0)
}
map_left, map_right, map_top, map_bottom = 0, 0, 0, 0
for line in infile.read().strip().split("\n"):
    d, dist, color = line.split(" ")
    for i in range(int(dist)):
        cur_pos = cur_pos[0] + deltas[d][0], cur_pos[1] + deltas[d][1]
        lagoon_map[cur_pos] = 1
        map_left = min(map_left, cur_pos[1])
        map_right = max(map_right, cur_pos[1])
        map_top = min(map_top, cur_pos[0])
        map_bottom = max(map_bottom, cur_pos[0])
flood_queue = deque()
flood_queue.append((map_top - 1, map_left - 1))
lagoon_map[(map_top - 1, map_left - 1)] = -1
area = (map_right - map_left + 3) * (map_bottom - map_top + 3) - 1
while flood_queue:
    cur_pos = flood_queue.popleft()
    for d in deltas:
        new_pos = cur_pos[0] + deltas[d][0], cur_pos[1] + deltas[d][1]
        if new_pos[0] >= map_top - 1 and new_pos[0] <= map_bottom + 1 and new_pos[1] >= map_left - 1 and new_pos[1] <= map_right + 1:
            if new_pos not in lagoon_map:
                lagoon_map[new_pos] = -1
                area -= 1
                flood_queue.append(new_pos)
print(area)
