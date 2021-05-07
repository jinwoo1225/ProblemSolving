def solution(m, n, puddles):
    board = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    board[1][1] = 1
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            print(i,j)
            if i + j == 2:
                continue
            if [j, i] in puddles:
                board[i][j] = 0
            else:
                board[i][j] = board[i][j - 1] + board[i - 1][j]
    return board[i][j] % 1000000007


print(solution(4, 3, [[2, 2]]))
