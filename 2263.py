from sys import stdin

N = int(stdin.readline())
inorder = list(map(int, stdin.readline().split()))
postorder = list(map(int, stdin.readline().split()))
# N = 7
# inorder = list(map(int, "4 2 5 1 6 3 7".split()))
# postorder = list(map(int, "4 5 2 6 7 3 1".split()))

root = postorder[-1]
inord_pos = {}

for i in range(N):
    inord_pos[inorder[i]] = i

answer = []

# inorder begin,end postorder begin, end
stack = [[0, N - 1, 0, N - 1]]

while stack:
    inord_begin, inord_end, postord_begin, postord_end = stack.pop()

    # CONQUER
    # root
    root = postorder[postord_end]
    # print
    answer.append(root)
    # 중위 순회의 루트!
    inord_root = inord_pos[root]

    # 왼쪽 부분
    left_size = inord_root - inord_begin

    # inORD LLLL   r    RRRRR
    # begin left  root  right end
    # poORD LLLL  RRRRR  r
    # begin left  right root  end

    # DIVIDE
    # 오른쪽이 나중
    if inord_root + 1 <= inord_end and postord_begin + left_size <= postord_end - 1:
        stack.append([inord_root + 1, inord_end, postord_begin + left_size, postord_end - 1])
    # 왼쪽이 처음( stack의 위에!)
    if inord_begin <= inord_root - 1 and postord_begin <= postord_begin + left_size - 1:
        stack.append([inord_begin, inord_root - 1, postord_begin, postord_begin + left_size - 1])

[print(a, end=" ") for a in answer]
