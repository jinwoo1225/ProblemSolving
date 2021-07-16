N = int(input())

graph = {}

for i in range(1, N + 1):
    graph[i] = set()

for i in range(N - 1):
    a, b = map(int, input().split())
    graph[a].add(b)
    graph[b].add(a)

visited = set()
result = [0 for _ in range(N + 1)]

stack = [1]

while stack:
    node = stack.pop()
    if node not in visited:
        visited.add(node)
        for next_node in graph[node]:
            if next_node not in visited:
                result[next_node] = node
                stack.append(next_node)

for r in result[2:]:
    print(r)
