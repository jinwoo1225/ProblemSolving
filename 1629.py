def fast_pow(n: int, k: int, mod: int) -> int:
    """
    faster power that uses Divide & Conquer
    :param n: base
    :param k: count
    :param mod: modular
    :return: powered n to k
    """
    if n == 0:
        raise ArithmeticError("n can't be 0")

    if k == 0:
        return 1

    temp: int = fast_pow(n, k // 2, mod)
    ret: int = (temp * temp) % mod

    if k % 2:
        ret = (ret * n) % mod
    return ret


a, b, c = map(int, input().split())

print(fast_pow(a, b, c))
