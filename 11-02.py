row_count = []
col_count = []
galaxies = []
while True:
    inputval = input()
    if not inputval:
        break
    row_count.append(0)
    for i, c in enumerate(inputval):
        if len(col_count) <= i:
            col_count.append(0)
        if c == "#":
            col_count[i] += 1
            row_count[-1] += 1
            galaxies.append((len(row_count) - 1, i))
row_real_coord = []
col_real_coord = []
cur_row_coord = 0
cur_col_coord = 0
for count in row_count:
    row_real_coord.append(cur_row_coord)
    cur_row_coord += 1000000 if count == 0 else 1
for count in col_count:
    col_real_coord.append(cur_col_coord)
    cur_col_coord += 1000000 if count == 0 else 1
total_dist = 0
for i, coord1 in enumerate(galaxies):
    for j, coord2 in enumerate(galaxies[i + 1:]):
        real_coord1 = row_real_coord[coord1[0]], col_real_coord[coord1[1]]
        real_coord2 = row_real_coord[coord2[0]], col_real_coord[coord2[1]]
        total_dist += abs(real_coord1[0] - real_coord2[0]) + abs(real_coord1[1] - real_coord2[1])
print(total_dist)
