INF = 987654321

import heapq


def solution(n: int, costs: list):
    graph = {}
    for a, b, cost in costs:
        graph.setdefault(a, {b: cost})
        graph.setdefault(b, {a: cost})
        graph[a][b] = cost
        graph[b][a] = cost

    visited = [False] * n

    def visit(node: int, queue: list) -> int:
        visited[node] = True
        for vertex, cost in graph[node].items():
            if not visited[vertex]:
                heapq.heappush(queue, [cost, vertex])

        new_queue = []
        for new_cost, new_vertex in queue:
            if not visited[new_vertex]:
                heapq.heappush(new_queue, [new_cost, new_vertex])

        queue = new_queue

        if len(queue) == 0:
            return 0

        next_cost, next_vertex = heapq.heappop(queue)
        return next_cost + visit(next_vertex, queue)

    return visit(0, [])


print(solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]))
