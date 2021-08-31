from itertools import permutations

N, M = map(int, input().split())
list(map(print, sorted(map(" ".join, set(permutations(sorted(input().split(), key=int), M))),
                       key=lambda x: list(map(int, x.split())))))
