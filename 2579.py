from sys import stdin

N = int(stdin.readline().strip())

# 한칸을 뛰거나 두칸을 뛰거나
# 연속한 3칸을 뛸수는 없습니다
# 계단의 갯수는 최대 300개

# 최댓값 300
step = [int(stdin.readline().strip()) for _ in range(N)]
step += [0] * (300 - len(step))

cacheJump = [0 for i in range(301)]
cacheJump[N - 1] = step[N - 1]

# 첫계단을 밟고 max(세번째?, 두번째?)

# 첫 계단
cacheJump[0] = step[0]
# 두번째 계단
cacheJump[1] = step[0] + step[1]
# 세번째 계단
cacheJump[2] = max(step[0] + step[2], step[1] + step[2])

# 네번째 계단 -> goes on
for t in range(3, N):
    cacheJump[t] = max(
        # 이전을 밟아서 하나만 밟음
        cacheJump[t - 2] + step[t],
        # 이전을 안 밟아서 두개 밟음
        cacheJump[t - 3] + step[t] + step[t - 1]
    )
print(cacheJump[N - 1])
