N, M, K = map(int, input().split())

board = [[0 for _ in range(M)] for _ in range(N)]

for i in range(K):
    y, x = map(int, input().split())
    board[y - 1][x - 1] = 1

visited = set()

size = 0

DY = (0, 0, 1, -1)
DX = (1, -1, 0, 0)


def dfs(y, x, s):
    stack = [(y, x)]
    while stack:
        _y, _x = stack.pop()
        s += 1
        for t in range(4):
            next_y = DY[t] + _y
            next_x = DX[t] + _x
            if 0 <= next_y < N and 0 <= next_x < M and board[next_y][next_x] == 1 and (next_y, next_x) not in visited:
                visited.add((next_y, next_x))
                stack.append((next_y, next_x))

    return s


for y in range(N):
    for x in range(M):
        if (y, x) not in visited and board[y][x] == 1:
            visited.add((y, x))
            size = max(size, dfs(y, x, 0))

print(size)
