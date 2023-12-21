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
box_array: list[list] = []
focal_lengths = {}
for i in range(256):
    box_array.append([])
for inp in inputs:
    if inp[-1] == "-":
        id = inp[:-1]
        hashval = hash_fn(id)
        if id in box_array[hashval]:
            box_array[hashval].remove(id)
    else:
        id, focal = inp.split("=")
        hashval = hash_fn(id)
        if id not in box_array[hashval]:
            box_array[hashval].append(id)
        focal_lengths[id] = int(focal)
for i, box in enumerate(box_array):
    for j, id in enumerate(box):
        total += (i + 1) * (j + 1) * focal_lengths[id]
print(total)
