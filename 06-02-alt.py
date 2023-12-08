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

left_bound = 0
right_bound = time // 2
while left_bound < right_bound:
    mid = (left_bound + right_bound) // 2
    score = mid * (time - mid)
    if score > distance:
        right_bound = mid
    else:
        left_bound = mid + 1
print(time + 1 - left_bound * 2)
