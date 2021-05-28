T = int(input())

arr = [0, 1, 1, 1, 2, 2] + [-1 for _ in range(95)]

for index in range(5, 101):
    arr[index] = arr[index - 1] + arr[index - 5]

for _ in range(T):
    N = int(input())
    print(arr[N])
