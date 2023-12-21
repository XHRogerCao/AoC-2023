total = 0
while True:
    rows = []
    columns = []
    while True:
        inputval = input()
        if not inputval:
            break
        rows.append(inputval)
        for i, c in enumerate(inputval):
            if len(columns) <= i:
                columns.append("")
            columns[i] += c
    if not rows:
        break
    for i in range(len(rows) - 1):
        row_diff = 0
        mirror_left, mirror_right = i, i + 1
        while mirror_left >= 0 and mirror_right < len(rows) and row_diff <= 1:
            for c1, c2 in zip(rows[mirror_left], rows[mirror_right]):
                if c1 != c2:
                    row_diff += 1
                    if row_diff >= 2:
                        break
            mirror_left -= 1
            mirror_right += 1
        if row_diff == 1:
            total += (i + 1) * 100
            break
    for i in range(len(columns) - 1):
        row_diff = 0
        mirror_left, mirror_right = i, i + 1
        while mirror_left >= 0 and mirror_right < len(columns) and row_diff <= 1:
            for c1, c2 in zip(columns[mirror_left], columns[mirror_right]):
                if c1 != c2:
                    row_diff += 1
                    if row_diff >= 2:
                        break
            mirror_left -= 1
            mirror_right += 1
        if row_diff == 1:
            total += (i + 1)
            break
print(total)
