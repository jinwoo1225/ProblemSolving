N, K = map(int, input().split())


def check(n: int):
    count = 0
    while True:
        div = n // 2
        mod = n % 2
        count += mod
        n = div
        if n == 0:
            break

    return count


if N <= K:
    print(0)
else:
    temp = N
    while True:
        if check(temp) <= K:
            print(temp - N)
            break
        else:
            temp += 1
