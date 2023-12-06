inputval = input()
seeds = list(map(int, inputval.split(":")[1].strip().split(" ")))
input()
maps = []
for i in range(7):
    input() # wasted line
    maps.append([])
    while True:
        inputval = input()
        if not inputval:
            break
        end_idx, start_idx, map_range = inputval.split(" ")
        maps[-1].append((int(start_idx), int(start_idx) + int(map_range), int(end_idx)))
for i in range(7):
    # print(f"{i}: {seeds}")
    new_dest = []
    for seed in seeds:
        found_map = False
        for start_head, start_end, end_head in maps[i]:
            if seed >= start_head and seed < start_end:
                found_map = True
                new_dest.append(seed - start_head + end_head)
                break
        if not found_map:
            new_dest.append(seed)
    seeds = new_dest
# print(f"{7}: {seeds}")
print(min(seeds))
