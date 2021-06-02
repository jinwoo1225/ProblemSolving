N = int(input())

arr = [int(i) for i in input().split()]

ans = [-1 for _ in range(N)]

stack = []

for i in range(N):
    while stack:
        if stack[-1][0] < arr[i]:
            num, index = stack.pop()
            ans[index] = arr[i]
        else:
            break

    stack.append((arr[i], i))

for a in ans:
    print(a, end=" ")