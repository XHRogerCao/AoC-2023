total = 0
while True:
    inputval = input()
    if not inputval:
        break
    springs, orders = inputval.split(" ")
    orders = map(int, orders.split(","))
    dp = {}
    def get_ways(sub_spring, combo, trailing_good):
        if len(sub_spring) == 0:
            if len(combo) == 0 or combo == (0,):
                return 1
            else:
                return 0
        if (sub_spring, combo, trailing_good) in dp:
            return dp[(sub_spring, combo, trailing_good)]
        if sub_spring[-1] == "#":
            if len(combo) == 0:
                return 0
            new_combo = list(combo)
            new_combo[-1] -= 1
            if new_combo[-1] < 0:
                # Contradiction; too many in a row
                dp[(sub_spring, combo, trailing_good)] = 0
                return 0
            new_combo = tuple(new_combo)
            dp[(sub_spring, combo, trailing_good)] = get_ways(sub_spring[:-1], new_combo, True)
            return dp[(sub_spring, combo, trailing_good)]
        elif sub_spring[-1] == ".":
            if trailing_good:
                if len(combo) != 0 and combo[-1] == 0:
                    dp[(sub_spring, combo, trailing_good)] = get_ways(sub_spring[:-1], combo[:-1], False)
                    return dp[(sub_spring, combo, trailing_good)]
                elif len(combo) != 0 and combo[-1] != 0:
                    # Contradiction
                    dp[(sub_spring, combo, trailing_good)] = 0
                    return 0
            dp[(sub_spring, combo, trailing_good)] = get_ways(sub_spring[:-1], combo, False)
            return dp[(sub_spring, combo, trailing_good)]
        else:
            dp[(sub_spring, combo, trailing_good)] = get_ways(sub_spring[:-1] + "#", combo, trailing_good) + get_ways(sub_spring[:-1] + ".", combo, trailing_good)
            return dp[(sub_spring, combo, trailing_good)]
    total += get_ways(springs, tuple(orders), False)

print(total)
