def hash_fn(s):
    total = 0
    for c in s:
        total += ord(c)
        total *= 17
        total = total % 256
    return total
total = 0
infile = open("input.txt", "r")
inputval = infile.read().strip()
inputs = inputval.split(",")
for inp in inputs:
    total += hash_fn(inp)
print(total)
