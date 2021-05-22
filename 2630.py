from sys import stdin

N = int(stdin.readline().strip())

board = []

for _ in range(N):
    board.append(list(map(int, stdin.readline().split())))

paper_dict = {
    0: 0,
    1: 0,
}


def check(piece: list):
    # piece 가 다 같은 element 인지 확인
    return len(set([ele for row in piece for ele in row])) == 1


def solve(y: int, x: int, size: int):
    if size <= 1:
        # if size is 1
        paper_dict[board[y][x]] += 1
        return

    new_piece = []
    for y_ in board[y:y + size]:
        new_piece.append(y_[x:x + size])

    if check(new_piece):
        # pass
        paper_dict[board[y][x]] += 1
    else:
        # not pass
        next_size = size // 2
        for dy in range(2):
            for dx in range(2):
                solve(y + (next_size * dy), x + (next_size * dx), next_size)


solve(0, 0, N)
print(paper_dict[0])
print(paper_dict[1])
