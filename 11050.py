N, K = map(int, input().split(' '))

def go(n : int, r: int) -> int:
    if n == r or r == 0:
        return 1
    return go(n-1, r-1) + go(n-1, r)

print(go(N,K))