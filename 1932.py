from sys import stdin

N = int(input())

triangle = [list(map(int, stdin.readline().split())) for a in range(N)]
cache = [[-1 for _ in range(N)] for _ in range(N)]


def find(y: int, x: int) -> int:
    global N
    if y >= N or x > y:
        return 0
    if cache[y][x] != -1:
        return cache[y][x]
    cache[y][x] = triangle[y][x] + max(find(y + 1, x), find(y + 1, x + 1))
    return cache[y][x]


print(find(0, 0))
