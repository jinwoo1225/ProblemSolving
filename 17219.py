from sys import stdin
N, M = map(int, input().split())

email_dict = {}

for _ in range(N):
    email, password = stdin.readline().strip().split()
    email_dict[email] = password

for _ in range(M):
    email = stdin.readline().strip()
    print(email_dict[email])