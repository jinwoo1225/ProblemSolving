from sys import stdin

N = int(stdin.readline())

min_cache = [0 for _ in range(3)]
max_cache = [0 for _ in range(3)]
max_precache = [0 for _ in range(3)]
min_precache = [0 for _ in range(3)]

for _ in range(N):
    line = list(map(int, stdin.readline().split()))

    # left
    max_precache[0] = max(max_cache[0], max_cache[1]) + line[0]
    min_precache[0] = min(min_cache[0], min_cache[1]) + line[0]

    # center
    max_precache[1] = max(max_cache[0], max_cache[1], max_cache[2]) + line[1]
    min_precache[1] = min(min_cache[0], min_cache[1], min_cache[2]) + line[1]

    # right
    max_precache[2] = max(max_cache[1], max_cache[2]) + line[2]
    min_precache[2] = min(min_cache[1], min_cache[2]) + line[2]

    max_cache = max_precache.copy()
    min_cache = min_precache.copy()

print(max(max_cache))
print(min(min_cache))
