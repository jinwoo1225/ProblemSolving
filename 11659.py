from sys import stdin

N, M = map(int, stdin.readline().split())

nums = list(map(int, stdin.readline().split()))
partial_sum = [0] * 100001
for index in range(1, N + 1):
    partial_sum[index] = partial_sum[index - 1] + nums[index - 1]

for _ in range(M):
    start, end = map(int, stdin.readline().split())
    print(partial_sum[end] - partial_sum[start - 1])
