from queue import PriorityQueue
from sys import stdin

N = int(input())
M = int(input())

graph = {}

for i in range(1, N + 1):
    graph[i] = {}

for m in range(M):
    start, end, cost = map(int, stdin.readline().split())
    if end not in graph[start]:
        graph[start][end] = cost
    else:
        if graph[start][end] > cost:
            graph[start][end] = cost

begin, end = map(int, stdin.readline().split())


def dijkstra(graph: dict, start: int) -> dict:
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = PriorityQueue()
    queue.put([0, start])

    while queue.qsize():
        cur_distance, cur_destination = queue.get()

        if distances[cur_destination] < cur_distance:
            continue

        for next_destination, next_distance in graph[cur_destination].items():
            distance = cur_distance + next_distance
            if distances[next_destination] > distance:
                distances[next_destination] = distance
                queue.put([distance, next_destination])

    return distances


print(dijkstra(graph, begin)[end])
