infile = open("input.txt", "r")

root = None
connections = {}
edges = []
for i, line in enumerate(infile.read().strip().split("\n")):
    component, wires = line.split(": ")
    wires = wires.split(" ")
    if root is None:
        root = component
    for wire in wires:
        if component not in connections:
            connections[component] = []
        if wire not in connections:
            connections[wire] = []
        connections[component].append(wire)
        connections[wire].append(component)
        edges.append((component, wire))
depths = {}
def calculate_edge(removed_edge):
    # dfs_tree = {}
    dfs_stack = [[root, 0, 0, 1, 0]]
    depths.clear()
    while dfs_stack:
        node, idx, depth, tree_size, max_depth = dfs_stack[-1]
        if node not in depths:
            depths[node] = depth
        # if node == "nvd":
        #     print("Check")
        if idx < len(connections[node]):
            wire = connections[node][idx]
            dfs_stack[-1][1] += 1
            if (node, wire) not in removed_edge and (wire, node) not in removed_edge:
                if wire in depths:
                    if len(dfs_stack) < 2 or wire != dfs_stack[-2][0]:
                        dfs_stack[-1][4] = min(dfs_stack[-1][4], depths[wire])
                else:
                    dfs_stack.append([wire, 0, depth + 1, 1, depth + 1])
        else:
            dfs_stack.pop()
            if dfs_stack:
                dfs_stack[-1][3] += tree_size
                dfs_stack[-1][4] = min(dfs_stack[-1][4], max_depth)
            if depth == max_depth:
                # Bridge is parent, return tree size
                return tree_size
print(len(edges))
for i, edge1 in enumerate(edges):
    if i < 116:
        continue # We already checked and can't find the answer here
    print(i)
    for j in range(i + 1, len(edges)):
        edge2 = edges[j]
        # if edge1 == ("cmg", "bvb") and edge2 == ("pzl", "hfx"):
        #     print("Check")
        size = calculate_edge([edge1, edge2])
        if size != len(connections):
            print(size * (len(connections) - size))
            exit(0)
