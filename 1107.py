N = int(input())
M = int(input())
broken = []
if M :
    broken = list(map(int, input().split()))
clicked = abs(N - 100)

# 100 < 500000 < 999999 < 1000000
for i in range(999999 + 1):
    able = True
    for j in str(i):
        if int(j) in broken:
            able = False
            break

    if able:
        clicked = min(clicked, abs(i - N) + len(str(i)))

print(clicked)
