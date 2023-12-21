import heapq
city_map = []
infile = open("input.txt", "r")
for line in infile.read().strip().split("\n"):
    city_map.append([])
    for c in line:
        city_map[-1].append(ord(c) - ord("0"))
min_heat = []
for i in range(3):
    min_heat.append([])
    for d in range(4):
        min_heat[-1].append([])
        for line in city_map:
            min_heat[-1][-1].append([])
            for c in line:
                min_heat[-1][-1][-1].append(-1)
min_heat[0][0][0][0] = 0
deltas = [
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0)
]
lava_heap = [(0, 0, 0, 0, 0)]
while lava_heap:
    dist, row, col, cons, cur_d = heapq.heappop(lava_heap)
    dirs_to_check = [(cur_d + 1) % 4, (cur_d + 3) % 4]
    if cons < 3:
        dirs_to_check.append(cur_d)
    for ndir in dirs_to_check:
        nrow, ncol = row + deltas[ndir][0], col + deltas[ndir][1]
        ncons = 1 if ndir != cur_d else cons + 1
        if ncol >= 0 and ncol < len(city_map[0]) and nrow >= 0 and nrow < len(city_map):
            if min_heat[ncons - 1][ndir][nrow][ncol] == -1:
                ndist = dist + city_map[nrow][ncol]
                min_heat[ncons - 1][ndir][nrow][ncol] = ndist
                if nrow == len(city_map) - 1 and ncol == len(city_map[0]) - 1:
                    print(ndist)
                    exit(0)
                heapq.heappush(lava_heap, (ndist, nrow, ncol, ncons, ndir))
