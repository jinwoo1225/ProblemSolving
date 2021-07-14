T = int(input())

for _ in range(T):
    sticker_size = int(input())

    stickers = [list(map(int, input().split())), list(map(int, input().split()))]

    cache = [
        [0] + [0] * sticker_size,
        [0] + [0] * sticker_size
    ]

    for i in range(sticker_size):
        cache[1][i + 1] = max(cache[0][i - 1], cache[0][i]) + stickers[1][i]
        cache[0][i + 1] = max(cache[1][i - 1], cache[1][i]) + stickers[0][i]

    print(max(cache[0][-1], cache[1][-1]))
