import numpy
infile = open("input.txt", "r")
hails = []
for i, line in enumerate(infile.read().strip().split("\n")):
    pos, vel = line.split(" @ ")
    pos = list(map(int, pos.split(", ")))
    vel = list(map(int, vel.split(", ")))
    hails.append((pos[0], pos[1], pos[2], vel[0], vel[1], vel[2]))
TOL = 1e-8
def validate(pos, vel):
    for hail in hails:
        t = None
        for i in range(3):
            if t is not None:
                if abs(pos[i] + vel[i] * t - hail[i] - hail[i + 3] * t) > TOL:
                    return False
            else:
                if vel[i] == hail[i + 3]:
                    if abs(pos[i] - hail[i]) > TOL:
                        return False
                else:
                    t = (hail[i] - pos[i]) / (vel[i] - hail[i + 3])
                    if t < 0:
                        return False
    return True
def solve(vx, vy):
    try:
        a = numpy.array([
            [1, 0, vx - hails[0][3], 0],
            [0, 1, vy - hails[0][4], 0],
            [1, 0, 0, vx - hails[1][3]],
            [0, 1, 0, vy - hails[1][4]],
        ])
        b = numpy.array([
            hails[0][0],
            hails[0][1],
            hails[1][0],
            hails[1][1],
        ])
        # [x, y, t1, t2]
        x = numpy.linalg.solve(a, b)
        a1 = numpy.array([
            [1, x[2]],
            [1, x[3]],
        ])
        b1 = numpy.array([
            hails[0][2] + hails[0][5] * x[2],
            hails[1][2] + hails[1][5] * x[3],
        ])
        # [z, vz]
        x1 = numpy.linalg.solve(a1, b1)
        return [round(x[0]), round(x[1]), round(x1[0]), vx, vy, round(x1[1])]
    except numpy.linalg.LinAlgError as e:
        return None
print(validate((24, 13, 10), (-2, 2, 2)))
vxa, vya = 0, 0
while True:
    for signx in [-1, 1]:
        for signy in [-1, 1]:
                vx, vy = vxa * signx, vya * signy
                if vx == -3 and vy == 1:
                    print("Check")
                sol = solve(vx, vy)
                if sol and validate(sol[:3], sol[3:]):
                    print(sol)
                    exit(0)
    # Do stuff with vx, vy, vz
    if vxa > 0:
        vxa, vya = vxa - 1, vya + 1
    else:
        vxa, vya = vya + 1, 0
