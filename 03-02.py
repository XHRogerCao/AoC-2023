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
                parts[-1].append((c, i))
    if number_sequence:
        numbers[-1].append((int(number_sequence), len(inputval) - len(number_sequence), len(inputval) - 1))
total = 0
for row, part_row in enumerate(parts):
    for part_id, x_pos in part_row:
        if part_id == "*":
            num_count = 0
            num_ratio = 1
            for i in range(row - 1, row + 2):
                if i >= 0 and i < len(numbers):
                    for val, start, end in numbers[i]:
                        if x_pos >= start - 1 and x_pos <= end + 1:
                            num_count += 1
                            num_ratio = val * num_ratio
            if num_count == 2:
                total += num_ratio
print(total)
