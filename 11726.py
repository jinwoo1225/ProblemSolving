
# https://www.acmicpc.net/source/29057643
N = int(input())
MOD = 10007
cache = [0,1,2]


for i in range(3, N + 1):
    cache.append(cache[i-2] + cache[i-1])


print(cache[N] % MOD)
