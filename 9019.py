from collections import deque

T = int(input())
visited = [False for _ in range(10001)]


def find(start: int, trg: int) -> str:
    queue = deque([[start, '']])
    visited[start] = True

    while queue:
        num, command = queue.popleft()
        # print(command)

        if num == trg:
            return command

        # D
        cur = (num * 2) % 10000
        if not visited[cur]:
            visited[cur] = True
            queue.append([cur, command + 'D'])

        # S
        cur = num - 1 if (num - 1) >= 0 else 9999
        if not visited[cur]:
            visited[cur] = True
            queue.append([cur, command + 'S'])

        # L
        cur = ((num % 1000) * 10) + num // 1000
        if not visited[cur]:
            visited[cur] = True
            queue.append([cur, command + 'L'])

        # R
        cur = (num // 10) + ((num % 10) * 1000)
        if not visited[cur]:
            visited[cur] = True
            queue.append([cur, command + 'R'])


for _ in range(T):
    first, target = map(int, input().split())
    visited = [False for _ in range(10001)]
    print(find(first, target))
