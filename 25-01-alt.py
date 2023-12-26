# Solution based on HyperNeutrino's answer.
# https://hyper-neutrino.xyz/

import random
from collections import deque
infile = open("input.txt", "r")

root = None
connections = {}
edges = {}
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
        order_index = min((component, wire), (wire, component))
        edges[order_index] = 0
depths = {}
for node1 in connections:
    for node2 in connections:
        if random.random() < 0.999:
            continue
        nodes = {node1: node1}
        bfs_queue = deque()
        bfs_queue.append(node1)
        while bfs_queue:
            cur_node = bfs_queue.popleft()
            if cur_node == node2:
                break
            for wire in connections[cur_node]:
                if wire not in nodes:
                    nodes[wire] = cur_node
                    bfs_queue.append(wire)
        cur_node = node2
        while cur_node != node1:
            new_node = nodes[cur_node]
            edges[min((cur_node, new_node), (new_node, cur_node))] += 1
            cur_node = new_node

edge_checks = []
for edge in edges:
    edge_checks.append((edges[edge], edge))
edge_checks.sort(reverse=True)
print(edge_checks[:10])
edges_to_remove = list(edge[1] for edge in edge_checks[:3])

total_size = len(connections)
bfs_queue = deque()
bfs_queue.append(root)
same_component = set([root])
while bfs_queue:
    cur_node = bfs_queue.popleft()
    for wire in connections[cur_node]:
        if (cur_node, wire) not in edges_to_remove and (wire, cur_node) not in edges_to_remove:
            if wire not in same_component:
                same_component.add(wire)
                bfs_queue.append(wire)
print(len(same_component) * (total_size - len(same_component)))
