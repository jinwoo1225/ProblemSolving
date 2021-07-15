n = int(input())

board = [[0 for _ in range(n)] for _ in range(n)]
count = 0


# 한줄에 하나씩 N개

def check(index, n):  # 행 열
    # 모든 행에 존재?
    if index == n:
        global count
        count += 1
        return

    for i in range(n):
        presense = 1
        for j in range(index):
            # 같은 열에 존재?
            if board[j][i] == 1:
                presense = 0
                break

        if presense == 1:
            leftrow = index  # 행
            leftcol = i  # 열
            while leftrow >= 0 and leftcol >= 0:
                if board[leftrow][leftcol] == 1:
                    presense = 0
                    break
                leftrow -= 1
                leftcol -= 1

        # 우 상단 대각선에 퀸이 있는지 확인
        if presense == 1:
            rightrow = index
            rightcol = i
            while rightrow >= 0 and rightcol < n:
                if board[rightrow][rightcol] == 1:
                    presense = 0
                    break
                rightrow -= 1
                rightcol += 1

        if presense == 0:
            # 퀸이 있다?
            continue
        board[index][i] = 1
        check(index + 1, n)  # 다음행에서 실행
        board[index][i] = 0


check(0, n)
print(count)
