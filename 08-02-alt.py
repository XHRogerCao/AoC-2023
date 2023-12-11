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

max_moves_allowed = len(lrinstruction) * len(nodes)

cycles = []
for node in current:
    moves = 0
    visited = {}
    is_done = False
    while not is_done:
        for i, inst in enumerate(lrinstruction):
            moves += 1
            if inst == "L":
                node = nodes[node][0]
            else:
                node = nodes[node][1]
            if node[-1] == "Z":
                if (node, i) in visited:
                    # Cycle count
                    cycles.append((moves - visited[node, i], visited))
                    is_done = True
                    break
                else:
                    visited[(node, i)] = moves
print(cycles)
