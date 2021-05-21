from sys import stdin

N = int(stdin.readline().strip())

image = []

for _ in range(N):
    image.append(stdin.readline().strip())


def check(piece: list) -> bool:
    return len(set([ele for row in piece for ele in row])) == 1


def quadtree(y: int, x: int, size: int) -> str:
    new_image = []
    for y_ in image[y:y + size]:
        new_image.append(y_[x:x + size])

    if check(new_image):
        return image[y][x]
    else:
        next_size = size // 2
        ret = '('
        for dy in range(2):
            for dx in range(2):
                ret += quadtree(y + (next_size * dy), x + (next_size * dx), next_size)

        return ret + ')'


print(quadtree(0, 0, N))
