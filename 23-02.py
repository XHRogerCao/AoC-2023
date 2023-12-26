infile = open("input.txt", "r")
snow_map = infile.read().strip().split("\n")
travelled = set()
max_dist = 0
deltas = [
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0)
]
dirs = [">", "v", "<", "^"]
# travelled.add((0, snow_map[0].find(".")))
node_map = {}
node_map[(0, snow_map[0].find("."))] = []
node_map[(len(snow_map) - 1, snow_map[-1].find("."))] = []
for i, row in enumerate(snow_map):
    for j, c in enumerate(row):
        if c != "#":
            neighbour_count = 0
            for delta in deltas:
                n_row, n_col = i + delta[0], j + delta[1]
                if n_row >= 0 and n_row < len(snow_map) and n_col >= 0 and n_col < len(snow_map[0]) and snow_map[n_row][n_col] != "#":
                    neighbour_count += 1
            if neighbour_count != 2 and neighbour_count != 0:
                node_map[(i, j)] = []
for row, col in node_map:
    for i, delta in enumerate(deltas):
        n_row, n_col = row + delta[0], col + delta[1]
        if n_row >= 0 and n_row < len(snow_map) and n_col >= 0 and n_col < len(snow_map[0]) and snow_map[n_row][n_col] != "#":
            dist = 1
            prev_dir = i
            while (n_row, n_col) not in node_map:
                for j, ndelta in enumerate(deltas):
                    if (j + 2) % 4 == prev_dir:
                        continue
                    nn_row, nn_col = n_row + ndelta[0], n_col + ndelta[1]
                    if nn_row >= 0 and nn_row < len(snow_map) and nn_col >= 0 and nn_col < len(snow_map[0]) and snow_map[nn_row][nn_col] != "#":
                        n_row, n_col = nn_row, nn_col
                        prev_dir = j
                        dist += 1
                        break
            node_map[(row, col)].append((dist, (n_row, n_col)))
def find_best_dist(row, col):
    if row == len(snow_map) - 1:
        return 0
    else:
        best_dist = None
        travelled.add((row, col))
        for edge_dist, new_coord in node_map[(row, col)]:
            if new_coord not in travelled:
                dist = find_best_dist(*new_coord)
                if dist is not None:
                    if best_dist is None:
                        best_dist = dist + edge_dist
                    else:
                        best_dist = max(best_dist, dist + edge_dist)
        travelled.remove((row, col))
        return best_dist
print(find_best_dist(0, snow_map[0].find(".")))
