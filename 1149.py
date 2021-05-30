from sys import stdin

N = int(stdin.readline())
rgb_board = [[0], [0], [0]]
cache = [
    [0] * (N + 1),  # R cache
    [0] * (N + 1),  # G cache
    [0] * (N + 1)   # B cache
]

# RGB
for _ in range(N):
    R, G, B = map(int, stdin.readline().split())
    rgb_board[0].append(R)
    rgb_board[1].append(G)
    rgb_board[2].append(B)

for index in range(1, N + 1):
    cache[0][index] = min(cache[1][index - 1], cache[2][index-1]) + rgb_board[0][index]
    cache[1][index] = min(cache[0][index - 1], cache[2][index-1]) + rgb_board[1][index]
    cache[2][index] = min(cache[0][index - 1], cache[1][index-1]) + rgb_board[2][index]


print(min(cache[0][N], cache[1][N], cache[2][N]))


# print(rgb_board)
