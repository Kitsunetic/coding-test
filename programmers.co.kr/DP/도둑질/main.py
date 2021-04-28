def solution(money):
    L = len(money)
    t = 2 + (L & 0x01)  # L이 홀/짝수일 때 dp의 column 수가 바뀜

    if L == 3:
        return max(money)

    dp = [[-1 for _ in range(t)] for _ in range(L)]
    mv = -1
    for j in range(t):
        dp[j][j] = money[j]
        mv = max(mv, money[j])
    for j in range(t):
        dp[2 + j][j] = money[j] + money[2 + j]
        mv = max(mv, money[j] + money[2 + j])

    for i in range(3, L - 1):
        for j in range(t):
            if not (0 <= i + j < L):
                break

            v = max(dp[i + j - 2][j], dp[i + j - 3][j]) + money[i + j]
            dp[i + j][j] = v
            mv = max(mv, v)

    return mv, dp
