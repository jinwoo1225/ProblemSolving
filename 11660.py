from sys import stdin

input = stdin.readline

N, M = map(int, input().split())

sums = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

for i in range(1, N + 1):
    temp = [0] + list(map(int, input().split()))
    for j in range(1, N + 1):
        sums[i][j] = temp[j] + sums[i - 1][j] + sums[i][j - 1] - sums[i - 1][j - 1]

for _ in range(M):
    y1, x1, y2, x2 = map(int, input().split())
    print(
        sums[y2][x2] - sums[y1 - 1][x2] - sums[y2][x1 - 1] + sums[y1 - 1][x1 - 1]
    )
