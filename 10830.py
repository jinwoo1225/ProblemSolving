N, B = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(N)]
MOD = 1000


def matrix_multiply(m: list, pow: int):
    ret = [[0 for _ in range(N)] for _ in range(N)]
    if pow == 1:
        # 하나일때
        return list(map(lambda x: list(map(lambda y: y % MOD, x)), m))
    elif pow % 2:
        # 나 * 나 - 1
        result = matrix_multiply(m, pow - 1)
        for x in range(N):
            for y in range(N):
                for t in range(N):
                    ret[x][y] += result[x][t] * m[t][y]
                ret[x][y] %= MOD

    else:
        # 나 * 나
        result = matrix_multiply(m, pow // 2)
        for x in range(N):
            for y in range(N):
                for t in range(N):
                    ret[x][y] += result[x][t] * result[t][y]
                ret[x][y] %= MOD

    return ret


list(map(print, map(lambda x: x.lstrip('[').rstrip(']').replace(', ', ' '), map(str, matrix_multiply(matrix, B)))))
