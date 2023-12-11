lrinstruction = input()
input()
nodes = {}
current = set()
while True:
    inputval = input()
    if not inputval:
        break
    node = inputval[0:3]
    left = inputval[7:10]
    right = inputval[12:15]
    nodes[node] = (left, right)
    if node[-1] == "A":
        current.add(node)
moves = 0
max_moves_allowed = len(lrinstruction) * len(nodes)
while True:
    for inst in lrinstruction:
        moves += 1
        new_current = set()
        all_z = True
        for cur_step in current:
            new_step = ""
            if inst == "L":
                new_step = nodes[cur_step][0]
            else:
                new_step = nodes[cur_step][1]
            new_current.add(new_step)
            if new_step[-1] != "Z":
                all_z = False
        current = new_current
        if all_z:
            print(moves)
            exit()
        # if moves > max_moves_allowed:
        #     print("error")
        #     print(max_moves_allowed)
        #     exit()
