words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

inputval = ""
tot = 0
while True:
    inputval = input()
    if not inputval:
        break
    first_digit = None
    last_digit = None
    for i, c in enumerate(inputval):
        for j, word in enumerate(words):
            if inputval[i:].startswith(word):
                # print(f"Found word: {word}")
                if first_digit is None:
                    first_digit = j + 1
                last_digit = j + 1
                break
        if ord(c) >= ord("0") and ord(c) <= ord("9"):
            if first_digit is None:
                first_digit = ord(c) - ord("0")
            last_digit = ord(c) - ord("0")
    tot += first_digit * 10 + last_digit
print(tot)
