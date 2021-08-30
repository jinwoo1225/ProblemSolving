def get_size_of_box(n: int) -> int:
    return n * n


Y, X = map(int, input().split())

max_size = min(Y, X)

board = [list(map(int, input())) for x in range(Y)]

size = 0
for y in range(Y):
    for x in range(X):
        for s in range(max_size):
            if y + s < Y and \
                    x + s < X and \
                    board[y][x] == board[y][x + s] and \
                    board[y][x] == board[y + s][x] and \
                    board[y][x] == board[y + s][x + s]:
                size = max(s, size)

print(get_size_of_box(size + 1))

"""

5 3
422
222
111
000
101
"""
"""
Input
5 10
9999999999
9999999999
9999999999
9999999999
9999999999

Answer
25
"""
