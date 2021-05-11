def DFS(graph: dict, start: int):
    visited = []
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            temp = sorted(graph[node] - set(visited), reverse=True)
            stack += temp

    return visited



N = int(input())
M = int(input())
infected = 1

graph = {}

for i in range(1, N+1):
    graph[i] = set()

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].add(b)
    graph[b].add(a)

print(len(DFS(graph, infected)) - 1)