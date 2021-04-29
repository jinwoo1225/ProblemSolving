n, k = map(int, input().split())

cash = []

for _ in range(n):
    cash.append(int(input()))

cash.sort(reverse=True)
ans = 0
for coin in cash:
    change = k // coin
    k -= coin * change
    ans += change

print(ans)
