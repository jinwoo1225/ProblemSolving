def back_track(stack):
    if len(stack) == m:
        print(' '.join(map(str, stack)))
        return

    for i in range(1, n+1):
        back_track(stack + [i])

n, m = map(int, input().split())

back_track([])