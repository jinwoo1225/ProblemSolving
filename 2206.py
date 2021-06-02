from collections import deque
from sys import stdin

N, M = map(int, stdin.readline().split())

board = [stdin.readline() for _ in range(N)]

#              y, x, d, breakable
queue = deque([[0, 0, 1, 1]])
distance = -1

DY = [0, 0, 1, -1]
DX = [1, -1, 0, 0]
visited = [[[False, False] for _ in range(M)]for _ in range(N)]

while queue:
    _y, _x, _d, _b = queue.popleft()
    if _y == N - 1 and _x == M - 1:
        distance = _d
        break
    if not visited[_y][_x][_b]:
        visited[_y][_x][_b] = True
        for t in range(4):
            next_y = _y + DY[t]
            next_x = _x + DX[t]
            if 0 <= next_y < N and 0 <= next_x < M:
                # break the wall or jump the wall  :)
                if board[next_y][next_x] == '1' and _b >= 1:
                    if not visited[next_y][next_x][0]:
                        queue.append([next_y, next_x, _d + 1, 0])
                elif board[next_y][next_x] == '0':
                    if not visited[next_y][next_x][_b]:
                        queue.append([next_y, next_x, _d + 1, _b])

print(distance)
