from itertools import combinations_with_replacement

_, M = map(int, input().split())
list(map(lambda p: print(" ".join(p)), combinations_with_replacement(sorted(list(input().split()), key=int), M)))
