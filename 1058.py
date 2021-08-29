INF = 987654321


def define_cost(a: list):
    return [1 if x == "Y" else INF for x in a]


def delete_same_index(a):
    a[1][a[0]] = 0
    return a[1]


def floyd(ls):
    n = len(ls)
    for f in range(n):
        for v in range(n):
            for t in range(n):
                if f == v or v == t or f == t:
                    continue
                elif ls[f][t] > ls[f][v] + ls[v][t]:
                    ls[f][t] = ls[f][v] + ls[v][t]
    return ls


def le_than(n: int, a: list):
    ret = []
    for element in a:
        ret.append(list(filter(lambda x: x <= n, element)))
    return ret


print(
    max(
        list(map(
            len,
            le_than(
                2,
                floyd(list(
                    map(delete_same_index,
                        enumerate(map(
                            define_cost,
                            map(list,
                                [input() for a in range(int(input()))])
                        )))
                ))
            )
        ))
    ) - 1
)

"""
3
NYY
YNN
YNN
"""
"""
4
NYYN
YNNN
YNNY
NNYN
"""
