N = int(input())
import sys

arr = []

for _ in range(N):
    X, Y = map(int, sys.stdin.readline().split())
    arr.append([X, Y])

arr.sort(key=lambda x: (x[1], x[0]))

for X, Y in arr:
    print(X, Y)
