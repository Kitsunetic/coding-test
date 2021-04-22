def arithmetic(A, B):
    S = set()

    for a in A:
        for b in B:
            for z in (a + b, a - b, a * b, a // b, b - a, b // a):
                if 0 < z and z <= 32000:
                    S.add(z)

    return S


def solution(N, number):
    dp = [set() for _ in range(9)]

    for i, m in enumerate([1, 11, 111, 1111, 11111], 1):
        v = N * m
        if number == v:
            return i
        dp[i].add(v)

    for d in range(2, 9):
        for i in range(1, d // 2 + 1):
            S = arithmetic(dp[i], dp[d - i])
            if number in S:
                return d

            dp[d].update(S)

    return -1
