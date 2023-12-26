import heapq
infile = open("input.txt", "r")
bricks = []
for i, line in enumerate(infile.read().strip().split("\n")):
    lcoord, rcoord = line.split("~")
    lfields = lcoord.split(",")
    rfields = rcoord.split(",")
    heapq.heappush(bricks, (int(lfields[2]), int(lfields[0]), int(lfields[1]), int(rfields[2]), int(rfields[0]), int(rfields[1]), i))
support_map = {}
support_by_map = {}
topdown = []
for i in range(10):
    topdown.append([None] * 10)
while bricks:
    brick = heapq.heappop(bricks)
    max_height = 0
    for i in range(brick[1], brick[4] + 1):
        for j in range(brick[2], brick[5] + 1):
            if topdown[i][j] and topdown[i][j][0] > max_height:
                max_height = topdown[i][j][0]
    support_by_map[brick[6]] = set()
    support_map[brick[6]] = set()
    brick_info = (max_height + brick[3] - brick[0] + 1, brick[6])
    # print(brick_info)
    for i in range(brick[1], brick[4] + 1):
        for j in range(brick[2], brick[5] + 1):
            if topdown[i][j] and topdown[i][j][0] == max_height:
                if topdown[i][j][1] not in support_map:
                    support_map[topdown[i][j][1]] = set()
                support_map[topdown[i][j][1]].add(brick[6])
                support_by_map[brick[6]].add(topdown[i][j][1])
            topdown[i][j] = brick_info
    # print(topdown)
# print(support_map)
# print(support_by_map)
count = 0
for i in support_map:
    if not support_map[i]:
        count += 1
    else:
        will_fall = False
        for top in support_map[i]:
            if len(support_by_map[top]) == 1:
                will_fall = True
                break
        if not will_fall:
            count += 1
print(count)

