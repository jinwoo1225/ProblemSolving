from collections import defaultdict, deque
import copy


def solution(tickets):
    answer = []
    N = len(tickets)
    graph = defaultdict(list)
    for start, end in tickets:
        graph[start].append(end)

    for key in graph:
        graph[key].sort()
    # airport, plan, graph_new
    queue = deque([['ICN', ['ICN'], graph]])

    while queue:
        airport, plan, new_graph = queue.popleft()

        if len(plan) == N + 1:
            return plan

        for next_a in new_graph[airport]:
            new_new_graph = copy.deepcopy(new_graph)
            new_new_graph[airport].remove(next_a)
            queue.append([next_a, plan + [next_a], new_new_graph])

    return answer