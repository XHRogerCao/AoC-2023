lrinstruction = input()
input()
nodes = {}
while True:
    inputval = input()
    if not inputval:
        break
    node = inputval[0:3]
    left = inputval[7:10]
    right = inputval[12:15]
    nodes[node] = (left, right)
moves = 0
current = "AAA"
while True:
    for inst in lrinstruction:
        moves += 1
        if inst == "L":
            current = nodes[current][0]
        else:
            current = nodes[current][1]
        if current == "ZZZ":
            print(moves)
            exit()
