import heapq

N, M = map(int, input().split())

graph = {}

for i in range(N):
    graph[i + 1] = {}

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1


def dijkstra(graph: dict, start: int) -> dict:
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start])

    while queue:
        current_distance, current_destination = heapq.heappop(queue)

        if distances[current_destination] < current_distance:
            continue

        for new_destination, new_distance in graph[current_destination].items():
            distance = current_distance + new_distance
            if distance < distances[new_destination]:
                distances[new_destination] = distance
                heapq.heappush(queue, [distance, new_destination])

    return distances


minimum = 987654321
answer = 0
for i in range(N):
    bacon = sum(dijkstra(graph, i + 1).values())
    if minimum > bacon:
        minimum = bacon
        answer = i + 1

print(answer)
