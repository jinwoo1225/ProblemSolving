# https://eda-ai-lab.tistory.com/509

import re
from itertools import permutations


def solution(expression: str) -> int:
    answer = []
    priority_operands = [x for x in ['+', '-', '*'] if x in expression]
    priority_operands = [list(y) for y in permutations(priority_operands)]
    ex = re.split(r'(\D)', expression)

    for operands in priority_operands:
        _ex = ex[:]
        for operand in operands:
            while operand in _ex:
                tmp = _ex.index(operand)
                _ex[tmp - 1] = str(eval(_ex[tmp - 1] + _ex[tmp] + _ex[tmp + 1]))
                print(_ex, tmp)
                input()
                _ex = _ex[:tmp] + _ex[tmp + 2:]
            print(_ex)
        answer.append(_ex[-1])
    return max(abs(int(x)) for x in answer)

print(solution("100-200*300-500+20"))
