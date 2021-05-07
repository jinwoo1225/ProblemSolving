import sys

M, N, inventory = map(int, input().split())

board = []

for _ in range(M):
    board.append(list(map(int, sys.stdin.readline().split())))


def check_flat(arr: list) -> bool:
    temp = -1
    for i in arr:
        for j in arr:
            if not temp == j and not temp == -1:
                return False
            temp = j
    return True

min_block = 987654321
max_block = -1
time = 0
answer = [987654321, 987654321]

for blocks in board:
    for block in blocks:
        min_block = min(block, min_block)
        max_block = max(block, max_block)

for target_height in range(min_block, max_block + 1):
    time = 0
    inv = inventory

    for i in range(len(board)):
        for j in range(len(board[0])):
            height = board[i][j] - target_height
            if height > 0:
                # 현재 블록이 목표치보다 큰가?
                time += height * 2
                # dig -> 2초
                inv += height
            elif height < 0:
                # 현재 블록이 목표치보다 작은가?
                time -= height
                # place -> 1초
                inv += height
                # 블럭을 놓았으므로 인벤토리에서 제거

    if inv >= 0:
        # 모든 블럭을 채웠을때 인벤토리가 음수면 패스~
        if time <= answer[0]:
            answer[0] = time
            answer[1] = target_height

print(answer[0], answer[1])

"""
3 4 1
64 38 64 64
64 64 40 64
64 64 64 63


3 4 1
64 64 64 64
64 64 64 64
64 64 64 63
"""
