# https://programmers.co.kr/learn/courses/30/lessons/42895#
# https://www.hamadevelop.me/algorithm-n-expression/
def solution(N, number):
    possible = [0, [N]]
    if N == number:
        return 1

    for num in range(2, 9):
        case = []
        appendi = int(str(N) * num)
        case.append(appendi)

        for key in range(1, num // 2 + 1):
            for a in possible[key]:
                for b in possible[num - key]:
                    case.append(a + b)
                    case.append(a - b)
                    case.append(b - a)
                    case.append(a * b)
                    case.append(a / b) if b else 0
                    case.append(b / a) if a else 0

            if number in case:
                return num
            possible.append(case)

    return -1
