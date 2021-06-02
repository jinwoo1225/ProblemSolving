from queue import PriorityQueue
from sys import stdin

input = stdin.readline

V, E = map(int, input().split())

graph = {}

start_node = int(input())

for i in range(1, V + 1):
    graph[i] = {}

for e in range(E):
    start, end, cost = map(int, input().split())
    try :
        graph[start][end]
        graph[start][end] = cost if cost < graph[start][end] else graph[start][end]
    except:
        graph[start][end] = cost


def dijkstra(graph: dict, start: int) -> dict:
    # start정점에서 각 정점을 리턴, 도달이 불가능 하면 float('inf') 무한대
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = PriorityQueue()
    queue.put([0, start])

    while queue.qsize():
        # 현재거리, 현재 위치
        cur_distance, cur_destination = queue.get()

        # 현재거리보다 저장된 거리가 짧으면 패스~
        if distances[cur_destination] < cur_distance:
            continue

        # 현재 위치에서 다른 정점 탐색
        for new_destination, new_distance in graph[cur_destination].items():
            distance = cur_distance + new_distance
            # 만약 다음노드 까지의 길이가 저장된 값보다 작다면?
            if distance < distances[new_destination]:
                distances[new_destination] = distance
                queue.put([distance, new_destination])

    return distances

answer = dijkstra(graph, start_node)


for e in range(1,V+1):
    print(answer[e] if not answer[e] == float('inf') else "INF")