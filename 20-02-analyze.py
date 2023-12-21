from collections import deque
infile = open("input.txt", "r")
modules = {}
for line in infile.read().strip().split("\n"):
    name, targets = line.split(" -> ")
    targets = targets.split(", ")
    module_type = "~"
    if name[0] == "%" or name[0] == "&":
        module_type = name[0]
        name = name[1:]

    if name not in modules:
        modules[name] = [[], "~", [], None]
    modules[name][1] = module_type
    modules[name][2] = targets
    for target in targets:
        if target not in modules:
            modules[target] = [[], "~", [], None]
        modules[target][0].append(name)
count = 0
rx_found = False
def find_dependency_branch(target, root):
    if modules[target][3] is None:
        modules[target][3] = []
    if root not in modules[target][3]:
        modules[target][3].append(root)
        for child in modules[target][2]:
            find_dependency_branch(child, root)
for target in modules["broadcaster"][2]:
    find_dependency_branch(target, target)
at_types = {}
for mod in modules:
    print(f"{modules[mod][1]}{mod}: {modules[mod][3]}")
    if modules[mod][1] == "&" and len(modules[mod][3]) == 1:
        if modules[mod][3][0] not in at_types:
            at_types[modules[mod][3][0]] = []
        at_types[modules[mod][3][0]].append(mod)
for mod in at_types:
    print(f"{mod}: {at_types[mod]}")
print(count)
