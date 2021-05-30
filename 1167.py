from sys import stdin

N = int(stdin.readline())

graph = {}

for i in range(1, N + 1):
    graph[i] = set()

for i in range(1, N + 1):
    inputs = list(map(int, input().split()))[:-1]
    edge, edges = inputs[0], inputs[1:]

    for j in range(0, len(edges), 2):
        graph[edge].add((edges[j], edges[j + 1]))

# classic DFS 1단 1에서 시작
max_distance = -1
max_node = 1
stack = [[max_node, 0]]
visited = set()

while stack:
    _n, _d = stack.pop()

    if _d > max_distance:
        max_distance = _d
        max_node = _n

    if _n not in visited:
        visited.add(_n)

        for node, distance in list(graph[_n]):
            if node not in visited:
                stack.append([node, _d + distance])

# DFS from farthest node
max_distance = 0
stack = [[max_node, 0]]
visited = set()
while stack:
    _n, _d = stack.pop()

    if _d > max_distance:
        max_distance = _d
        max_node = _n

    if _n not in visited:
        visited.add(_n)

        for node, distance in list(graph[_n]):
            if node not in visited:
                stack.append([node, _d + distance])

print(max_distance)
