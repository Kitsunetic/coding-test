def arithmetic(A, B):
    S = set()
    for a in A:
        for b in B:
            for v in (a + b, a - b, a * b, a // b, b - a, b // a):
                if 0 < v <= 32000:
                    S.add(v)

    return S


def solution(N, number):
    dp = [set() for _ in range(9)]
    dp[1].add(N)

    for i in range(2, 9):
        v = int(f"{N}" * i)
        if v == number:
            return i
        dp[i].add(v)

        for j in range(1, i // 2 + 1):
            S = arithmetic(dp[j], dp[i - j])
            if number in S:
                return i

            dp[i].update(S)

    return -1
