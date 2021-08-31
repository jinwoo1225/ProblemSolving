import operator
from functools import reduce

input()
print(reduce(operator.add, map(operator.mul,
                               sorted(list(map(int, input().split()))),
                               sorted(list(map(int, input().split())), reverse=True))))
