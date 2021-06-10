def solution(n, results):
    answer = 0

    graph = {}

    for i in range(1, n + 1):
        graph[i] = {i: 0}

    for start, end in results:
        graph[start][end] = 1

    result_graph = {}
    for i in range(1, n + 1):
        result_graph[i] = {}
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if j not in graph[i]:
                result_graph[i][j] = float('inf')
            else:
                result_graph[i][j] = graph[i][j]

    for via in range(1, n + 1):
        for start in range(1, n + 1):
            for end in range(1, n + 1):
                if result_graph[start][via] + result_graph[via][end] < result_graph[start][end]:
                    result_graph[start][end] = result_graph[start][via] + result_graph[via][end]

    # print(graph)
    for i in range(1, n + 1):
        cnt = 0
        for j in range(1, n + 1):
            if result_graph[i][j] != float('inf') or result_graph[j][i] != float('inf'):
                cnt += 1

        if cnt == n:
            answer += 1

    return answer


print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))
