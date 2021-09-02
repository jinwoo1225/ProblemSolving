R, C, K = map(int, input().split())

board = [input() for _ in range(R)]

visited = set()
visited.add((R - 1, 0))

moves = []
DY = (0, 0, 1, -1)
DX = (1, -1, 0, 0)


def dfs(y, x, move):
    global R, C
    if y == 0 and x == C - 1:
        moves.append(move)
        return

    for t in range(4):
        next_y = DY[t] + y
        next_x = DX[t] + x
        if 0 <= next_y < R and 0 <= next_x < C and board[next_y][next_x] == '.' and (next_y, next_x) not in visited:
            visited.add((next_y, next_x))
            dfs(next_y, next_x, move + 1)
            visited.remove((next_y, next_x))


dfs(R - 1, 0, 1)
print(len(list(filter(lambda x: x == K, moves))))
