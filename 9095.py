T = int(input())

max_num: int = 11
cache = [0 for i in range(12)]


def solve(i: int) -> None:
    global max_num
    if i > max_num:
        return
    cache[i] += 1
    solve(i + 1)
    solve(i + 2)
    solve(i + 3)


solve(0)

for _ in range(T):
    print(cache[int(input())])
