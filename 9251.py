A = input()
B = input()

answer = [[0 for _ in range(len(B) + 1)] for _ in range(len(A) + 1)]

for i in range(1, len(A) + 1):
    for j in range(1, len(B) + 1):
        if A[i - 1] == B[j - 1]:
            # 같을 때
            answer[i][j] = 1 + answer[i - 1][j - 1]
        else:
            # 다를 때
            answer[i][j] = max(answer[i][j - 1], answer[i - 1][j])

print(answer[-1][-1])