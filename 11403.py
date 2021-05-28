from collections import deque
N = int(input())

graph = []
graph_dict = {}

for i in range(N):
    graph_dict[i] = set()

for _ in range(N):
    graph.append(list(map(int, input().split())))

for index,part in enumerate(graph):
    for sub_index, connected in enumerate(part):
        if connected:
            graph_dict[index].add(sub_index)


for index in range(N):
    queue = deque(list(graph_dict[index]))
    visited = set()
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            queue+= list(graph_dict[node] - visited)

    for j in range(N):
        print(1 if j in visited else 0, end=" ")
    print()
