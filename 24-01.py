infile = open("input.txt", "r")
hails = []
for i, line in enumerate(infile.read().strip().split("\n")):
    pos, vel = line.split(" @ ")
    pos = list(map(int, pos.split(", ")))
    vel = list(map(int, vel.split(", ")))
    hails.append((pos[0], pos[1], vel[0], vel[1]))
count = 0
MIN_RANGE = 200000000000000
MAX_RANGE = 400000000000000
def sign(x):
    return 1 if x > 0 else -1
for i, hail_a in enumerate(hails):
    for j in range(i + 1, len(hails)):
        hail_b = hails[j]
        slope_a = hail_a[3] / hail_a[2]
        slope_b = hail_b[3] / hail_b[2]
        numerator = hail_a[1] - hail_b[1] + slope_b * hail_b[0] - slope_a * hail_a[0]
        if slope_a == slope_b:
            if numerator == 0:
                count += 1
                continue
            else:
                continue
        x_int = numerator / (slope_b - slope_a)
        y_int = hail_a[1] + slope_a * (x_int - hail_a[0])
        # print(f"({i},{j}): x={x_int}; y={y_int}")
        if x_int < MIN_RANGE or x_int > MAX_RANGE or y_int < MIN_RANGE or y_int > MAX_RANGE:
            continue # Out of range
        if (x_int - hail_a[0]) * sign(hail_a[2]) < 0:
            continue
        if (x_int - hail_b[0]) * sign(hail_b[2]) < 0:
            continue
        count += 1
print(count)
