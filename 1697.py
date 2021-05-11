# BFS 로 세가지 경우 검색
# 0 100000


from collections import deque


def BFS(start: int, track: int) -> int:
    count = 0
    queue = deque([[start, count]])

    while queue:
        node, cnt = queue.popleft()
        count = cnt
        if not visited[node]:
            visited[node] = True
            if node == track:
                return count

            count += 1
            # 순간이동!
            if node * 2 <= 100000:
                queue.append([node * 2, count])
            # 앞
            if node + 1 <= 100000:
                queue.append([node + 1, count])
            # 뒤
            if node - 1 >= 0:
                queue.append([node - 1, count])

    return count


N, M = map(int, input().split())
visited = [False] * 100001
print(BFS(N, M))
