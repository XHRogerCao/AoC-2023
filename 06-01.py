raw_time = input().split(" ")
raw_distance = input().split(" ")
times = []
distances = []
for i, val in enumerate(raw_time):
    if i == 0:
        continue
    if val:
        times.append(int(val))
for i, val in enumerate(raw_distance):
    if i == 0:
        continue
    if val:
        distances.append(int(val))
total = 1
for time, distance in zip(times, distances):
    count = 0
    for i in range(time):
        if i * (time - i) > distance:
            count += 1
    total *= count
print(total)
