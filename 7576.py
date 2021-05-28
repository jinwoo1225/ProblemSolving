from collections import deque
from sys import stdin

NX, MY = map(int, stdin.readline().split())

box = []
visited = [[False for i in range(NX)] for j in range(MY)]
queue: deque = deque()
days = 0
DY = [0, 0, 1, -1]
DX = [1, -1, 0, 0]

for _ in range(MY):
    box.append(list(map(int, stdin.readline().split())))

for y in range(MY):
    for x in range(NX):
        if box[y][x] == 1:
            queue.append([y, x, 0])

# print(box)

if not queue:
    flag: bool = True
    for y in box:
        if 0 in y:
            print(-1)
            flag = False
            break

    if flag:
        print(0)
else:
    while queue:
        _y, _x, _d = queue.popleft()

        if _y >= MY or _y < 0 or _x >= NX or _x < 0:
            # print('off the wall')
            continue

        if box[_y][_x] == -1:
            continue

        if not visited[_y][_x]:
            visited[_y][_x] = True
            days = _d
            box[_y][_x] = 1
            for d in range(4):
                queue.append([_y + DY[d], _x + DX[d], _d + 1])

    flag: bool = True
    for y in box:
        if 0 in y:
            print(-1)
            flag = False
            break

    if flag:
        print(days)
