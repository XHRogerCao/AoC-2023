total = 0
while True:
    inputval = input()
    if not inputval:
        break
    numbers = list(map(int, inputval.split(" ")))
    last_num = [numbers[-1]]
    all_zero = False
    while not all_zero:
        all_zero = True
        new_numbers = []
        for i in range(len(numbers) - 1):
            new_numbers.append(numbers[i + 1] - numbers[i])
            if new_numbers[-1] != 0:
                all_zero = False
        last_num.append(new_numbers[-1])
        numbers = new_numbers
    total += sum(last_num)
print(total)
