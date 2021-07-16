import math

from sys import stdin

input = stdin.readline


class SegmentTree:
    size: int
    tree: list

    def __init__(self, initial_state: list):
        self.size = 2 ** (int(math.ceil(math.log(len(initial_state), 2))) + 1)
        self.tree = [0 for _ in range(self.size)]

        for index, node in enumerate(initial_state):
            self.tree[(self.size // 2) + index] = node

        self.construct()

    def construct(self) -> None:
        for i in range((self.size // 2 - 1), 0, -1):
            self.tree[i] = self.tree[i * 2] + self.tree[i * 2 + 1]

    def update(self, index: int, value: int) -> None:
        index += self.size // 2 - 1
        self.tree[index] = value
        while index > 1:
            index //= 2
            self.tree[index] = self.tree[index * 2] + self.tree[index * 2 + 1]

    def get(self, left: int, right: int, node_index: int, node_left: int, node_right: int) -> int:
        if right < node_left or node_right < left:
            return 0
        elif left <= node_left and node_right <= right:
            return self.tree[node_index]
        mid = (node_left + node_right) // 2
        return self.get(left, right, node_index * 2, node_left, mid) + self.get(left, right, node_index * 2 + 1,
                                                                                mid + 1, node_right)


N, M, K = map(int, input().split())
segTree = SegmentTree([int(input()) for _ in range(N)])

for _ in range(M + K):
    a, b, c = map(int, input().split())
    if a == 1:
        segTree.update(b, c)
    else:
        print(segTree.get(b - 1, c - 1, 1, 0, segTree.size // 2 - 1))
