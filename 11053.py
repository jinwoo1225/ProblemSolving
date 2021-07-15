N = int(input())
numbers = list(map(int, input().split()))

size = [0] * N

for i in range(N):
    for j in range(i):
        # 나보다 뒤에 친구들
        if numbers[i] > numbers[j] and size[i] < size[j]:
            size[i] = size[j]
    size[i] += 1

print(max(size))
