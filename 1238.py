from queue import PriorityQueue
from sys import stdin

input = stdin.readline
N, M, F = map(int, input().split())

graph = {}
reversed_graph = {}

for i in range(1, N + 1):
    graph[i] = {}
    reversed_graph[i] = {}

for _ in range(M):
    start, end, time = map(int, input().split())
    graph[start][end] = time
    reversed_graph[end][start] = time


# dijkstra made by PriorityQueue
# returns distances from start
def dijkstra(graph: dict, start: int) -> dict:
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = PriorityQueue()
    queue.put([distances[start], start])

    while queue.qsize():
        # distance, destination
        cur_dis, cur_des = queue.get()

        # 현재 거리가 기존 거리보다 크다? 패스~
        if distances[cur_des] < cur_dis:
            continue

        for new_des, new_dis in graph[cur_des].items():
            dis = cur_dis + new_dis
            if dis < distances[new_des]:
                distances[new_des] = dis
                queue.put([dis, new_des])

    return distances


# 파티에서 집까지
dij = dijkstra(graph, F)
# 집에서 파티까지
rev_dij = dijkstra(reversed_graph, F)

max_distance = -1
for i in range(1, N + 1):
    max_distance = max(max_distance, dij[i] + rev_dij[i])

print(max_distance)
