from collections import deque

N, K = map(int, input().split())

MAX_SIZE = 100001

# position
queue = deque([N])
visited_time = [0 for _ in range(MAX_SIZE)]
visited_time[N] = 1

while queue:
    position = queue.popleft()

    if position == K:
        print(visited_time[position] - 1)
        break

    if position * 2 < MAX_SIZE and not visited_time[position * 2]:
        queue.appendleft(position * 2)
        visited_time[position * 2] = visited_time[position]

    if position + 1 < MAX_SIZE and not visited_time[position + 1]:
        queue.append(position + 1)
        visited_time[position + 1] = visited_time[position] + 1

    if 0 <= position - 1 and not visited_time[position - 1]:
        queue.append(position - 1)
        visited_time[position - 1] = visited_time[position] + 1
