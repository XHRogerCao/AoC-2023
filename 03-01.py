numbers = []
parts = []
row_num = 0
while True:
    inputval = input()
    if not inputval:
        break
    number_sequence = ""
    numbers.append([])
    parts.append([])
    for i, c in enumerate(inputval):
        if c.isnumeric():
            number_sequence += c
        else:
            if number_sequence:
                numbers[-1].append((int(number_sequence), i - len(number_sequence), i - 1))
                number_sequence = ""
            if c != ".":
                parts[-1].append(i)
    if number_sequence:
        numbers[-1].append((int(number_sequence), len(inputval) - len(number_sequence), len(inputval) - 1))
total = 0
for row, number_row in enumerate(numbers):
    for part_no, start, end in number_row:
        is_adjacent = False
        for i in range(row - 1, row + 2):
            if i >= 0 and i < len(parts):
                for x_pos in parts[i]:
                    if x_pos >= start - 1 and x_pos <= end + 1:
                        is_adjacent = True
                        break
        if is_adjacent:
            total += part_no
print(total)
