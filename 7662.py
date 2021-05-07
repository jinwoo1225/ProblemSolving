import heapq
import sys


def up_down_heap(operations):
    max_heap = []
    min_heap = []
    for operation in operations:
        operand, command = operation.split()
        if operand == "I":
            # insert
            heapq.heappush(max_heap, -int(command))
            heapq.heappush(min_heap, int(command))
        else:
            # deletion
            if min_heap:
                if command == '-1':
                    # min heap pop
                    min = heapq.heappop(min_heap)
                    max_heap.remove(-min)
                    heapq.heapify(max_heap)
                else:
                    max = heapq.heappop(max_heap)
                    min_heap.remove(-max)
                    heapq.heapify(min_heap)
    if not min_heap:
        return [0, 0]
    else:
        return [-max_heap[0], min_heap[0]]


T = int(input())

for _ in range(T):
    N = int(input())
    operations = []
    for op in range(N):
        operations.append(sys.stdin.readline().rstrip('\n'))

    max_h, min_h = up_down_heap(operations)
    if max_h == 0 and min_h == 0:
        print("EMPTY")
    else:
        print(max_h, min_h)
