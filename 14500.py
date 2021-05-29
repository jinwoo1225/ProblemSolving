N, M = map(int, input().split())

board = []

DY = (0, 0, 1, -1)
DX = (1, -1, 0, 0)

max_num: int = -1
visited = set()


def DFS(_y: int, _x: int, _d: int, _s: int) -> None:
    global max_num
    if _d >= 3:
        max_num = max(max_num, _s)
        return

    visited.add((_y, _x))

    for t in range(4):
        ny, nx = _y + DY[t], _x + DX[t]
        if 0 <= ny < N and 0 <= nx < M and (ny, nx) not in visited:
            DFS(ny, nx, _d + 1, _s + board[ny][nx])

    visited.remove((_y, _x))


for i in range(N):
    board.append(list(map(int, input().split())))

for y in range(N):
    for x in range(M):
        # normal DFS
        DFS(y, x, 0, board[y][x])
        # ㅓ ㅏ ㅜ ㅗ 는 DFS로 못찾죠?
        # ㅓ
        if y < N - 2 and 1 <= x:
            max_num = max(max_num, board[y][x] + board[y + 1][x] + board[y + 2][x] + board[y + 1][x - 1])

        # ㅏ
        if y < N - 2 and x < M - 1:
            max_num = max(max_num, board[y][x] + board[y + 1][x] + board[y + 2][x] + board[y + 1][x + 1])

        # ㅜ
        if y < N - 1 and x < M - 2:
            max_num = max(max_num, board[y][x] + board[y][x + 1] + board[y][x + 2] + board[y + 1][x + 1])

        # ㅗ(욕아님 ㅎ)
        if 1 <= y and x < M - 2:
            max_num = max(max_num, board[y][x] + board[y][x + 1] + board[y][x + 2] + board[y - 1][x + 1])


print(max_num)
