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
while not rx_found:
    count += 1
    pulses = deque()
    pulses.append(("button", "broadcaster", False))
    while pulses:
        source, target, is_high = pulses.popleft()
        if target == "rx" and not is_high:
            rx_found = True
            break
        if modules[target][1] == "%":
            if modules[target][3] is None:
                modules[target][3] = False
            if not is_high:
                modules[target][3] = not modules[target][3]
                for next_target in modules[target][2]:
                    pulses.append((target, next_target, modules[target][3]))
        elif modules[target][1] == "&":
            if modules[target][3] is None:
                modules[target][3] = [False] * len(modules[target][0])
            modules[target][3][modules[target][0].index(source)] = is_high
            signal_to_send = not all(modules[target][3])
            for next_target in modules[target][2]:
                pulses.append((target, next_target, signal_to_send))
        else:
            for next_target in modules[target][2]:
                pulses.append((target, next_target, is_high))
print(count)
