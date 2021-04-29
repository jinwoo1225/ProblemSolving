N = int(input())
members = []

for i in range(N):
    members.append(input().split())

members.sort(key=lambda x: int(x[0]))

for member in members:
    print(member[0], member[1])