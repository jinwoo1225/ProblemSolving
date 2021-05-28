from sys import stdin
from queue import PriorityQueue

T = int(stdin.readline())
abs_min_heap = PriorityQueue()
for _ in range(T):
    n = int(stdin.readline())

    if n:
        abs_min_heap.put((abs(n), n))
    else:
        if abs_min_heap.qsize():
            print(abs_min_heap.get()[1])
        else:
            print(0)
