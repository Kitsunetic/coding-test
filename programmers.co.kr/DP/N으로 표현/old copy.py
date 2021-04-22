def arithmetic(A, B):
    S = set()

    for a in A:
        for b in B:
            for z in (a + b, a - b, a * b, a // b, b - a, b // a):
                if 0 < z and z <= 32000:
                    S.add(z)

    return S


def solution(N, number):
    inf = 9999
    dp = [inf for _ in range(999999)]
    ds = [set() for _ in range(9)]

    for i, m in enumerate([1, 11, 111, 1111, 11111], 1):
        dp[N * m] = i
        ds[i].add(N * m)

    for d in range(2, 9):
        for i in range(1, d // 2 + 1):
            j = d - i

            S = arithmetic(ds[i], ds[j])
            for s in S:
                if dp[s] > d:
                    dp[s] = d
                    ds[d].add(s)
    return -1 if dp[number] == inf else dp[number]
