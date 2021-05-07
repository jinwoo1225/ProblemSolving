N, K = map(int, input().split())

idx = 0
chairs = [x for x in range(N)]
answer = []

while chairs:
    idx += K - 1
    idx %= len(chairs)
    answer.append(chairs.pop(idx) + 1)

print("<" + str(answer)[1:-1] + ">")