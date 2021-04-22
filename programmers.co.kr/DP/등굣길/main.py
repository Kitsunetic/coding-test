def solution(m, n, puddles):
    dp = [[0 for _ in range(m)] for _ in range(n)]  # dp[n][m]
    dp[0][0] = 1

    # 가로/세로축
    for i in range(m):
        if [i + 1, 1] in puddles:
            break
        dp[0][i] = 1
    for i in range(n):
        if [1, i + 1] in puddles:
            break
        dp[i][0] = 1

    for x in range(1, m):
        for y in range(1, n):
            if [x + 1, y + 1] in puddles:
                continue

            dp[y][x] = dp[y - 1][x] + dp[y][x - 1]

    return dp[n - 1][m - 1] % 1000000007
