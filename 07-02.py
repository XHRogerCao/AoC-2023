hands = []
def calculateHandType(hand):
    counter = {}
    for c in hand:
        if c not in counter:
            counter[c] = 0
        counter[c] += 1
    jokers = counter.get("J", 0)
    if "J" in counter:
        del counter["J"]
    cards = list(sorted(counter.values(), reverse=True))
    if len(cards) > 0:
        cards[0] += jokers
    else:
        cards.append(jokers)
    if cards[0] == 5:
        return 7
    elif cards[0] == 4:
        return 6
    elif cards[0] == 3:
        if cards[1] == 2:
            return 5
        return 4
    elif cards[0] == 2:
        if cards[1] == 2:
            return 3
        return 2
    return 1
card_order = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
card_rank = {}
def get_cards_rank(cards):
    result = []
    for c in cards:
        result.append(card_rank[c])
    return tuple(result)
for i, c in enumerate(card_order):
    card_rank[c] = len(card_order) - i
while True:
    inputval = input()
    if not inputval:
        break
    cards, bet = inputval.split(" ")
    hands.append((calculateHandType(cards), get_cards_rank(cards), int(bet)))
hands.sort()
total = 0
for i, hand in enumerate(hands):
    total += (i + 1) * hand[2]
print(total)
