from sys import stdin

N, M = map(int, stdin.readline().strip().split())

graph = {}
count = 0
visited = []

for n in range(1, N + 1):
    graph[n] = set()

for _ in range(M):
    a, b = map(int, stdin.readline().strip().split())
    graph[a].add(b)
    graph[b].add(a)


def DFS(start: int) -> None:
    stack = [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack += list(graph[node] - set(visited))


for n in range(1, N + 1):
    if n not in visited:
        count += 1
        DFS(n)

print(count)
