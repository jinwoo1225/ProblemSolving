from sys import stdin

N = int(stdin.readline().strip())

query = []

for _ in range(N):
    query.append(list(map(int, stdin.readline().split())))

query.sort(key=lambda x: (x[1], x[0]))

time = 0
answer = []
for q in query:
    start, end = q
    if start >= time:
        time = end
        answer.append(q)

print(len(answer))