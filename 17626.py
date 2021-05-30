N = int(input())

cache = [0] * (N + 1)

cache[1] = 1

for i in range(2, N + 1):
    minV: int = 987654321
    j = 1
    while j ** 2 <= i:
        minV = min(minV, cache[i - j * j])
        j += 1
    cache[i] = minV + 1

print(cache[N])
