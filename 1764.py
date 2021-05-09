import sys

N, M = map(int, input().split())
never_heard = set()
never_seen = set()

for _ in range(N):
    never_heard.add(sys.stdin.readline().strip())

for _ in range(M):
    never_seen.add(sys.stdin.readline().strip())

print(len(never_heard & never_seen))
print("\n".join(sorted(list(never_heard & never_seen))))
