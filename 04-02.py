total = 0
cards = [1]
current_id = 0
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
    while len(cards) <= current_id + win_count:
        cards.append(1)
    for i in range(win_count):
        cards[current_id + 1 + i] = cards[current_id + 1 + i] + cards[current_id]
    total += cards[current_id]
    current_id += 1
print(total)
