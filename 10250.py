T = int(input())
for t in range(T):
    H, W, N = map(int, input().split())
    k = 0
    for w in range(W):
        for h in range(H):
            k += 1
            if k == N:
                print(f'{h + 1}{w + 1:02}')
                break
        if k == N:
            break

