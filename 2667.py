from sys import stdin

N = int(stdin.readline().strip())

apartments = [stdin.readline().strip() for _ in range(N)]

visited = [[False for _ in range(N)] for _ in range(N)]

DY = [0, 0, 1, -1]
DX = [1, -1, 0, 0]


def DFS(y: int, x: int) -> int:
    if visited[y][x]:
        return 0

    stack = [[y, x]]
    count = 0
    global N
    while stack:
        _y, _x = stack.pop()

        if _y >= N or _y < 0 or _x >= N or _x < 0:
            continue

        if apartments[_y][_x] == '0':
            continue

        if not visited[_y][_x]:
            visited[_y][_x] = True
            count += 1
            for t in range(4):
                stack.append([_y + DY[t], _x + DX[t]])

    return count


apartments_count = 0
answer = []
for y in range(N):
    for x in range(N):
        if not visited[y][x] and apartments[y][x] == '1':
            apartments_count += 1
            answer.append(DFS(y, x))

print(apartments_count)
for a in sorted(answer):
    print(a)
