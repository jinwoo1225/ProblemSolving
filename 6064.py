from sys import stdin

T = int(stdin.readline().strip())


def gcd(a: int, b: int) -> int:
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def lcm(a: int, b: int)->int:
    return (a * b) // gcd(a, b)


for _ in range(T):
    M, N, x, y = map(int, stdin.readline().split())
    max_num = lcm(M, N)

    while True:
        if max_num < x and max_num < y:
            print('-1')
            break
        if x == y:
            print(x)
            break

        elif x > y:
            y += N
        elif x < y:
            x += M
