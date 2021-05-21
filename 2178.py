from collections import deque
from sys import stdin

N, M = map(int, stdin.readline().split())

board = []

for _ in range(N):
    board.append(stdin.readline().strip())

visited = [[False for _ in range(M)] for _ in range(N)]
distance = 987654321

DY = [0, 0, 1, -1]
DX = [1, -1, 0, 0]

queue = deque([[0, 0, 1]])

while queue:
    # y좌표, x좌표, distance
    _y, _x, _d = queue.popleft()
    # print(_y, _x, _d)

    if _y < 0 or _y >= N or _x < 0 or _x >= M:
        # off the wall
        continue

    if board[_y][_x] == '0':
        # visited a wall |-|-|
        continue

    if _y == N - 1 and _x == M - 1:
        # made it!
        # print('made it!')
        distance = min(_d, distance)

    if not visited[_y][_x]:
        visited[_y][_x] = True
        for t in range(4):
            queue.append([_y + DY[t], _x + DX[t], _d + 1])


print(distance)
