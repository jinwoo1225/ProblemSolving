import math
N, R = map(int, input().split())
print(math.factorial(N)//(math.factorial(N-R) * math.factorial(R)))
