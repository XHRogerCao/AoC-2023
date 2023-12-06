inputval = input()
seeds_input = list(map(int, inputval.split(":")[1].strip().split(" ")))
seeds = []
for i in range(0, len(seeds_input), 2):
    seeds.append((seeds_input[i], seeds_input[i] + seeds_input[i + 1]))
seeds.sort()
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
    maps[-1].sort()
for i in range(7):
    # print(f"{i}: {seeds}")
    new_dest = []
    seed_idx = 0
    map_idx = 0
    while seed_idx < len(seeds):
        seed_start, seed_end = seeds[seed_idx]
        if map_idx >= len(maps[i]):
            new_dest.append((seed_start, seed_end))
            seed_idx += 1
            continue
        map_start, map_end, map_dest = maps[i][map_idx]
        if map_end <= seed_start:
            map_idx += 1
        elif map_start <= seed_start:
            if seed_end <= map_end:
                new_dest.append((seed_start - map_start + map_dest, seed_end - map_start + map_dest))
                seed_idx += 1
            else:
                new_dest.append((seed_start - map_start + map_dest, map_end - map_start + map_dest))
                seeds[seed_idx] = (map_end, seed_end)
        else:
            if seed_end <= map_start:
                new_dest.append((seed_start, seed_end))
                seed_idx += 1
            else:
                new_dest.append((seed_start, map_start))
                seeds[seed_idx] = (map_start, seed_end)
    new_dest.sort()
    seeds = new_dest
# print(f"{7}: {seeds}")
print(len(seeds))
print(min(seeds))
