T = int(input())

def wear(clothes):
    answer = 1
    cloth_dict = {}
    for _, clothType in clothes:
        try:
            cloth_dict[clothType]
            cloth_dict[clothType] += 1
        except KeyError:
            cloth_dict[clothType] = 2
    for key in cloth_dict.keys():
        answer *= cloth_dict[key]
    return answer - 1

for _ in range(T):
    N = int(input())
    clothes = []
    for k in range(N):
        clothes.append(input().split())

    print(wear(clothes))

