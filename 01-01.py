inputval = ""
tot = 0
while True:
    inputval = input()
    if not inputval:
        break
    first_digit = None
    last_digit = None
    for c in inputval:
        if ord(c) >= ord("0") and ord(c) <= ord("9"):
            if first_digit is None:
                first_digit = ord(c) - ord("0")
            last_digit = ord(c) - ord("0")
    tot += first_digit * 10 + last_digit
print(tot)
