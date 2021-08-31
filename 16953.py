from collections import deque

A, B = map(int, input().split())

queue = deque([(A, 1)])

count = -1

while queue:
    num, move = queue.popleft()
    if num == B:
        count = move
        break

    if num > B:
        continue

    queue.append((num * 2, move + 1))
    queue.append((num * 10 + 1, move + 1))

print(count)
