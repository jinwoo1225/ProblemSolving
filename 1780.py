import sys

n = int(sys.stdin.readline())
paper = [[]]
for y in range(n):
    paper.append([0] + list(map(int, sys.stdin.readline().split())))

answer_dict = {
    -1: 0,
    0: 0,
    1: 0,
    None: 0
}


def check(piece: list) -> bool:
    return len(set([ele for y in piece for ele in y])) == 1


def solve(y: int, x: int, size: int) -> None:
    new_piece = []
    for y_ in paper[y:y + size]:
        new_piece.append(y_[x:x + size])
    # 사이즈가 1이면 검증할것이 하나!
    if size == 1:
        answer_dict[paper[y][x]] += 1
        return

    if check(new_piece):
        answer_dict[paper[y][x]] += 1
    else:
        # 다음 사이즈는 3을 나눈것!
        nextsize = size // 3
        # 각 9개의 종이를 검사!
        for y_ in range(3):
            for x_ in range(3):
                solve(y + (nextsize * y_), x + (nextsize * x_), nextsize)


solve(1, 1, n)
print(answer_dict[-1])
print(answer_dict[0])
print(answer_dict[1])
