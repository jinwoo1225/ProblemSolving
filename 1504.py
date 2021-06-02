from queue import PriorityQueue
from sys import stdin

N, E = map(int, input().split())

graph = {}

for i in range(1, N + 1):
    graph[i] = {}

for e in range(E):
    start, end, cost = map(int, stdin.readline().split())
    graph[start][end] = cost
    graph[end][start] = cost

V1, V2 = map(int, input().split())


def dijkstra(graph: dict, start: int) -> dict:
    distances = {node : float('inf') for node in graph}
    distances[start] = 0
    queue = PriorityQueue()
    queue.put([distances[start], start])

    while queue.qsize():
        cur_distance, cur_destination = queue.get()

        if distances[cur_destination] < cur_distance:
            continue

        for new_destination, new_distance in graph[cur_destination].items():
            distance = cur_distance + new_distance
            if distance < distances[new_destination]:
                distances[new_destination] = distance
                queue.put([distance, new_destination])

    return distances


one_to_v = dijkstra(graph, 1)
v1 = dijkstra(graph, V1)
v2 = dijkstra(graph, V2)

route = [
    one_to_v[V1] + v1[V2] + v2[N],
    one_to_v[V2] + v2[V1] + v1[N]
]

print(min(route) if not min(route) == float('inf') else -1)
