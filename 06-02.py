raw_time = input().split(" ")
raw_distance = input().split(" ")
time = ""
distance = ""
for i, val in enumerate(raw_time):
    if i == 0:
        continue
    if val:
        time += val
for i, val in enumerate(raw_distance):
    if i == 0:
        continue
    if val:
        distance += val
time = int(time)
distance = int(distance)
total = 1
count = 0
for i in range(time):
    if i * (time - i) > distance:
        count += 1
total *= count
print(total)
