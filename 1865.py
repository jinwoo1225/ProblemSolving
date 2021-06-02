from sys import stdin


def bellman_ford(graph: dict, start: int):
    distances: dict = {node: 100000 for node in graph}
    distances[start] = 0
    for i in range(len(distances) - 1):
        for node in graph:
            for neighbor in graph[node]:
                # 현재 거쳐가는 정점의 거리가 더 적을 경우
                distance = distances[node] + graph[node][neighbor]
                distances[neighbor] = distance if distances[neighbor] > distance else distances[neighbor]

    for node in graph:
        for neighbor in graph[node]:
            distance = distances[node] + graph[node][neighbor]
            if distances[neighbor] > distance:
                return False

    return True


TC = int(input())

for _ in range(TC):
    N, M, W = map(int, input().split())

    graph = {}

    for i in range(1, N + 1):
        graph[i] = {}

    for i in range(M):
        start, end, cost = map(int, stdin.readline().split())
        if end not in graph[start]:
            graph[start][end] = graph[end][start] = cost
        else:
            graph[start][end] = graph[end][start] = cost if cost < graph[start][end] else graph[start][end]

    for w in range(W):
        start, end, cost = map(int, stdin.readline().split())
        graph[start][end] = -cost

    # is flag True, it is time-travel!!

    print('NO' if bellman_ford(graph, 1) else "YES")
