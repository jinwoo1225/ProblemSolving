from collections import deque
from sys import stdin

NX, MY, H = map(int, stdin.readline().split())

box = []
visited = [[[False for i in range(NX)] for j in range(MY)] for h in range(H)]
queue: deque = deque()
days = 0
DH = [0, 0, 0, 0, 1, -1]
DY = [0, 0, 1, -1, 0, 0]
DX = [1, -1, 0, 0, 0, 0]
for _h in range(H):
    temp = []
    for _ in range(MY):
        temp.append(list(map(int, stdin.readline().split())))
    box.append(temp)

for h in range(H):
    for y in range(MY):
        for x in range(NX):
            if box[h][y][x] == 1:
                queue.append([h, y, x, 0])

# print(box)

if not queue:
    flag: bool = True
    for h in box:

        if not flag:
            break
        for y in h:
            if 0 in y:
                print(-1)
                flag = False
                break

    if flag:
        print(0)
else:
    while queue:
        _h, _y, _x, _d = queue.popleft()

        if box[_h][_y][_x] == -1:
            continue

        if not visited[_h][_y][_x]:
            visited[_h][_y][_x] = True
            days = _d
            box[_h][_y][_x] = 1
            for d in range(6):
                if _h + DH[d] >= H or _h + DH[d] < 0 \
                        or _y + DY[d] >= MY or _y + DY[d] < 0 \
                        or _x + DX[d] >= NX or _x + DX[d] < 0:
                    # print('off the wall')
                    continue
                queue.append([_h + DH[d], _y + DY[d], _x + DX[d], _d + 1])

    flag: bool = True
    for h in box:
        if not flag:
            break
        for y in h:
            if 0 in y:
                print(-1)
                flag = False
                break

    if flag:
        print(days)
