import re
infile = open("input.txt", "r")
workflows = {}
in_pattern = re.compile("(.+)\{(.+)\}")
obj_pattern = re.compile("\{x=(.+),m=(.+),a=(.+),s=(.+)\}")
input_p1, input_p2 = infile.read().strip().split("\n\n")
field_names = {"x":0,"m":1,"a":2,"s":3}
for line in input_p1.split("\n"):
    res = in_pattern.fullmatch(line)
    flow_id, flow_data = res.group(1, 2)
    workflows[flow_id] = []
    rules = flow_data.split(",")
    for i, rule in enumerate(rules):
        if i == len(rules) - 1:
            workflows[flow_id].append((0, "~", 0, rule))
        else:
            cond, pipe = rule.split(":")
            workflows[flow_id].append((field_names[cond[0]], cond[1], int(cond[2:]), pipe))
def find_total(pipe, min_bounds, max_bounds):
    min_bounds, max_bounds = list(min_bounds), list(max_bounds)
    if pipe == "R":
        return 0
    elif pipe == "A":
        total = 1
        for a, b in zip(min_bounds, max_bounds):
            total *= max(b - a + 1, 0)
        return total
    else:
        for a, b in zip(min_bounds, max_bounds):
            if b < a:
                return 0
        total = 0
        for field_idx, op, base_val, new_pipe in workflows[pipe]:
            if op == "<":
                new_max_bounds = list(max_bounds)
                if new_max_bounds[field_idx] < base_val:
                    total += find_total(new_pipe, min_bounds, new_max_bounds)
                    break
                else:
                    new_max_bounds[field_idx] = base_val - 1
                    total += find_total(new_pipe, min_bounds, new_max_bounds)
                    min_bounds[field_idx] = base_val
            elif op == ">":
                new_min_bounds = list(min_bounds)
                if new_min_bounds[field_idx] > base_val:
                    total += find_total(new_pipe, new_min_bounds, max_bounds)
                    break
                else:
                    new_min_bounds[field_idx] = base_val + 1
                    total += find_total(new_pipe, new_min_bounds, max_bounds)
                    max_bounds[field_idx] = base_val
            else:
                total += find_total(new_pipe, min_bounds, max_bounds)
        return total
print(find_total("in", [1] * 4, [4000] * 4))
