from sys import stdin

N, M = map(int, stdin.readline().split())

truth_teller = set(list(map(int, input().split()))[1:])
parties = []
for _ in range(M):
    parties += [set(list(map(int, input().split()))[1:])]

while True:
    flag = True
    for party in parties:
        if party & truth_teller:
            truth_teller |= party
            parties.remove(party)
            flag = False

    if flag:
        break

print(len(parties))