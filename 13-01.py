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
        if rows[i] == rows[i + 1]:
            # Could be mirror; validate
            is_mirror = True
            mirror_left, mirror_right = i, i + 1
            while mirror_left >= 0 and mirror_right < len(rows):
                if rows[mirror_left] != rows[mirror_right]:
                    is_mirror = False
                    break
                mirror_left -= 1
                mirror_right += 1
            if is_mirror:
                total += (i + 1) * 100
                break
    for i in range(len(columns) - 1):
        if columns[i] == columns[i + 1]:
            # Could be mirror; validate
            is_mirror = True
            mirror_left, mirror_right = i, i + 1
            while mirror_left >= 0 and mirror_right < len(columns):
                if columns[mirror_left] != columns[mirror_right]:
                    is_mirror = False
                    break
                mirror_left -= 1
                mirror_right += 1
            if is_mirror:
                total += (i + 1)
                break
print(total)
