from sys import stdin

N: int = int(input())

graph: dict = {}
for i in range(1, N + 1):
    graph[i] = {}

for _ in range(N - 1):
    start, end, cost = map(int, stdin.readline().split())

    graph[start][end] = cost
    graph[end][start] = cost

# 가장 먼 노드 두개의 길이가 곧 트리의 지름
# 따라서 어디서 시작하던지 상관이 없지요~
start: int = 1
stack: list = [[0, start]]
visited: set = set()
farthest_node: int = 1
max_length: int = -1

while stack:
    _d, node = stack.pop()

    if _d > max_length:
        max_length = _d
        farthest_node = node

    if node not in visited:
        visited.add(node)
        for next_node in graph[node]:
            if next_node not in visited:
                stack.append([_d + graph[node][next_node], next_node])

stack = [[0, farthest_node]]
visited = set()
max_length = -1

while stack:
    _d, node = stack.pop()

    if _d > max_length:
        max_length = _d

    if node not in visited:
        visited.add(node)
        for next_node in graph[node]:
            if next_node not in visited:
                stack.append([_d + graph[node][next_node], next_node])

print(max_length)
