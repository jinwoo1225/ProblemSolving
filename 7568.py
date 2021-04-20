T = int(input())
L = []
for t in range(T):
    L.append(list(map(int, input().split())))

rank = [1] * T

for i in range(len(L)):
    for j in range(len(L)):
        if i == j:
            continue
        x = L[i][0]
        y = L[i][1]
        p = L[j][0]
        q = L[j][1]
        if x < p and y < q:
            rank[i] += 1

for i in range(len(rank)):
    print(rank[i], end=" " if i < len(rank) - 1 else "\n")
