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
total = 0
for line in input_p2.split("\n"):
    res = obj_pattern.match(line)
    obj_data = tuple(map(int, res.group(1, 2, 3, 4)))
    cur_pipe = "in"
    while cur_pipe != "R" and cur_pipe != "A":
        for field_idx, op, base_val, new_pipe in workflows[cur_pipe]:
            if op == ">":
                if obj_data[field_idx] > base_val:
                    cur_pipe = new_pipe
                    break
            elif op == "<":
                if obj_data[field_idx] < base_val:
                    cur_pipe = new_pipe
                    break
            else:
                cur_pipe = new_pipe
                break
    if cur_pipe == "A":
        total += sum(obj_data)
print(total)
