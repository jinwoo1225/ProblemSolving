from collections import deque
from sys import stdin

d = deque()
N = input()

for i in map(int, stdin):
    d.append(i) if i else d.pop()
print(sum(d))
