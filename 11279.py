import sys
from queue import PriorityQueue

heap = PriorityQueue()

N = int(input())

querys = []

for _ in range(N):
    querys.append(int(sys.stdin.readline().strip()))

for query in querys:
    if heap.empty() and query == 0:
        print(0)
    elif query == 0:
        print(-heap.get())
    else:
        heap.put(-query)
