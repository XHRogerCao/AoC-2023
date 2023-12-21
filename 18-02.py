import bisect
infile = open("input.txt", "r")
deltas = [
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0)
]
symbols = {"R": 0, "D": 1, "L": 2, "U": 3}
cur_pos = (0, 0)
vertical_lines = {}
total_area = 0
for line in infile.read().strip().split("\n"):
    d, dist, color = line.split(" ")
    # Old way so it's a lot more comprehensible
    # dist, d = int(dist), symbols[d]

    # New way
    dist, d = int(color[2:7], base=16), int(color[7], base=16)
    print(f"Dir={d}, dist={dist}")
    new_pos = cur_pos[0] + dist * deltas[d][0], cur_pos[1] + dist * deltas[d][1]
    if new_pos[1] == cur_pos[1]:
        r_start, r_end, col = min(new_pos[0], cur_pos[0]), max(new_pos[0], cur_pos[0]) + 1, new_pos[1]
        if r_start not in vertical_lines:
            vertical_lines[r_start] = []
        if r_end - 1 not in vertical_lines:
            vertical_lines[r_end - 1] = []
        if r_end not in vertical_lines:
            vertical_lines[r_end] = []
        vertical_lines[r_start].append(("+", (col, r_start, r_end)))
        vertical_lines[r_end].append(("-", (col, r_start, r_end)))
    cur_pos = new_pos
cur_line = None
cur_bars = []
print("")
for line in sorted(vertical_lines.keys()):
    if cur_line is not None:
        height = line - cur_line
        top_width = 0
        bottom_width = 0
        # 0: outside; 1: completely inside;
        # 2: on the line, top is inside; 3: on the line, bottom is inside
        line_status = 0
        start_col = None
        for col, r_start, r_end in cur_bars:
            if cur_line != r_start and cur_line != r_end - 1:
                # Cross a vertical line. Flip area
                if line_status:
                    top_width += col - start_col
                    bottom_width += col - start_col
                    line_status = 0
                else:
                    start_col = col
                    line_status = 1
                    top_width += 1
                    bottom_width += 1
            elif cur_line == r_start:
                # Cross a line that starts. Consider all cases
                if line_status == 0:
                    line_status = 3
                    start_col = col
                    top_width += 1
                    bottom_width += 1
                elif line_status == 1:
                    line_status = 2
                    top_width += col - start_col
                    bottom_width += col - start_col
                    start_col = col
                elif line_status == 2:
                    line_status = 1
                    top_width += col - start_col
                    bottom_width += 1
                    start_col = col
                elif line_status == 3:
                    line_status = 0
                    top_width += col - start_col
                    bottom_width += col - start_col
                    start_col = col
            else:
                # Cross a line that ends. Consider all cases
                if line_status == 0:
                    line_status = 2
                    start_col = col
                    top_width += 1
                elif line_status == 1:
                    line_status = 3
                    top_width += col - start_col
                    bottom_width += col - start_col
                    start_col = col
                elif line_status == 2:
                    line_status = 0
                    top_width += col - start_col
                    start_col = col
                elif line_status == 3:
                    line_status = 1
                    top_width += col - start_col
                    start_col = col

        if line_status != 0:
            # Something went wrong; investigate the line
            print(f"Error at line {cur_line}; status {line_status}")
        print(cur_bars)
        print(f"{top_width}+({height}-1)x{bottom_width}={top_width + (height - 1) * bottom_width}")
        total_area += top_width + (height - 1) * bottom_width
    cur_line = line
    print(f"Cur_line={cur_line}")
    for op, data in vertical_lines[line]:
        if op == "+":
            bisect.insort(cur_bars, data)
        else:
            cur_bars.remove(data)
print(total_area)
