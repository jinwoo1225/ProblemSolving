from sys import stdin

default = int('11111111111111111111', 2)
answer_default = int('00000000000000000000', 2)
answer = answer_default
N = int(stdin.readline())
for _ in range(N):
    query = stdin.readline().strip().split()
    if query[0] == 'add':
        answer |= 2 ** (int(query[1]) - 1)
    elif query[0] == 'remove':
        answer &= default - (2 ** (int(query[1]) - 1))
    elif query[0] == 'check':
        print((answer >> (int(query[1]) - 1)) % 2)
    elif query[0] == 'toggle':
        answer ^= (2 ** (int(query[1]) - 1))
    elif query[0] == 'all':
        answer = default
    elif query[0] == 'empty':
        answer = answer_default
