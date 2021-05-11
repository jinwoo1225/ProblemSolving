# 패턴
pattern = int(input())

# ioi
ioi_size = int(input())
ioi_target = input()

answer = 0
index = 1
pattern_cnt = 0

# 오직 O(N)만에 끝내야함
# I[-1] O[0] I[1]
while index < ioi_size - 1:
    if ioi_target[index - 1] == "I" and ioi_target[index] == 'O' and ioi_target[index + 1] == "I":
        pattern_cnt += 1
        if pattern_cnt == pattern:
            pattern_cnt -= 1
            answer += 1
        index += 1
    else:
        pattern_cnt = 0
    index += 1

print(answer)
