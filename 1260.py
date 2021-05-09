N, M, start = map(int, input().split())

graph = {}

for i in range(1, N + 1):
    graph[i] = set()

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].add(b)
    graph[b].add(a)


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


from collections import deque


def BFS(graph: dict, start: int):
    visited = []
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            temp = sorted(graph[node] - set(visited))
            queue += temp

    return visited


print(str(DFS(graph, start)).lstrip('[').rstrip(']').replace(',', ''))
print(str(BFS(graph, start)).lstrip('[').rstrip(']').replace(',', ''))
