total = 0
while True:
    inputval = input()
    if not inputval:
        break
    winning = []
    numbers = []
    win_count = 0
    card_num, rest = inputval.split(":")
    wins, nums = rest.split("|")
    for val in wins.strip().split(" "):
        if val:
            winning.append(int(val))
    for val in nums.strip().split(" "):
        if val:
            numbers.append(int(val))

    for num in numbers:
        if num in winning:
            win_count += 1
    if win_count > 0:
        total += 2 ** (win_count - 1)
print(total)
