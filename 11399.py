N = int(input())
arr = map(int, input().split())
answer_arr = []
answer = 0

for a in sorted(arr):
    answer += a
    answer_arr.append(answer)


print(sum(answer_arr))

