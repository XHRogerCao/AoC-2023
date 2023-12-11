total = 0
while True:
    inputval = input()
    if not inputval:
        break
    numbers = list(map(int, inputval.split(" ")))
    first_num = [numbers[0]]
    all_zero = False
    while not all_zero:
        all_zero = True
        new_numbers = []
        for i in range(len(numbers) - 1):
            new_numbers.append(numbers[i + 1] - numbers[i])
            if new_numbers[-1] != 0:
                all_zero = False
        first_num.append(new_numbers[0])
        numbers = new_numbers
    total += sum(val * ((i % 2) * -2 + 1) for i, val in enumerate(first_num))
print(total)
