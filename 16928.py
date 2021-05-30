from collections import deque

N, M = map(int, input().split())

ladder_dict = {}
snake_dict = {}

for _ in range(N):
    start, end = map(int, input().split())
    ladder_dict[start] = end

for _ in range(M):
    start, end = map(int, input().split())
    snake_dict[start] = end

player = 1

queue = deque([[1, 0]])
visited = set()
while queue:
    cursor, move = queue.popleft()

    if cursor == 100:
        print(move)
        break

    if cursor not in visited:
        visited.add(cursor)

        if cursor in ladder_dict.keys():
            cursor = ladder_dict[cursor]
        elif cursor in snake_dict.keys():
            cursor = snake_dict[cursor]

        for d in range(1, 6 + 1):
            # Next Cursor
            NC = cursor + d
            if NC not in visited:
                queue.append([NC, move + 1])
