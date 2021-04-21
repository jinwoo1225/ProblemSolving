def solution(clothes):
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


print(
    solution([ ["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))

# keys = options.keys()
# values = (options[key] for key in keys)
# combinations = [dict(zip(keys, combination)) for combination in itertools.product(*values)]
