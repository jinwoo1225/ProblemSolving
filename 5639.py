import sys

sys.setrecursionlimit(10 ** 9)

input_list = []
while len(input_list) <= 10000:
    try:
        input_list.append(int(input()))
    except EOFError:
        break


def find(start, end):
    # 이분탐색
    if start > end:
        return

    div = end + 1

    for i in range(start + 1, end + 1):
        if input_list[start] < input_list[i]:
            div = i
            # 반띵
            break

    find(start + 1, div - 1)
    find(div, end)
    # 노드의 머리.
    print(input_list[start])


find(0, len(input_list) - 1)
