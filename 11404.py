n = int(input())  # 도시의 개수
m = int(input())  # 버스의 개수

# 플로이드 와샬 알고리즘

INF = 98564321

graph = [[INF for _ in range(n)] for _ in range(n)]

for i in range(n):
    graph[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a - 1][b - 1] = min(c, graph[a - 1][b - 1])

for mid in range(n):
    for lo in range(n):
        for hi in range(n):
            if graph[lo][mid] + graph[mid][hi] < graph[lo][hi]:
                graph[lo][hi] = graph[lo][mid] + graph[mid][hi]

for i in range(n):
    for j in range(n):
        print(0 if graph[i][j] == INF else graph[i][j], end=" " if j != n - 1 else "")
    print()
