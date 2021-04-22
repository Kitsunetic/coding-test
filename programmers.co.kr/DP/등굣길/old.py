"""
옛날에는 거리까지 저장하려고 하니까 코드가 좀 더 길어졌던 것 같다.
"""

from queue import Queue
from itertools import product


def solution(m, n, puddles):
    # dp = [[[0xffffffff, 0]] * (m+1)] * (n+1) # 거리, 방법의 수
    dp = [[[0xFFFFFFFF, 0, False] for i in range(m + 1)] for i in range(n + 1)]
    q = Queue()

    dp[1][1] = [0, 1, True]
    q.put((1, 1))
    while not q.empty():
        y, x = q.get()
        # print('current', y, x)

        for dy, dx in [[y + 1, x], [y, x + 1]]:
            if [dx, dy] not in puddles and dy <= n and dx <= m:
                if dp[dy][dx][2]:
                    dp[dy][dx][0] = dp[y][x][0] + 1
                    dp[dy][dx][1] = dp[dy][dx][1] + dp[y][x][1]
                    if dp[dy][dx][1] > 1000000007:
                        dp[dy][dx][1] %= 1000000007
                    dp[dy][dx][2] = True
                else:
                    dp[dy][dx][0] = dp[y][x][0] + 1
                    dp[dy][dx][1] = dp[dy][dx][1] + dp[y][x][1]
                    if dp[dy][dx][1] > 1000000007:
                        dp[dy][dx][1] %= 1000000007
                    dp[dy][dx][2] = True
                    q.put((dy, dx))

    # for y in range(1, n+1):
    #    for x in range(1, m+1):
    #        print(dp[y][x][1], '', end='')
    #    print()

    return dp[n][m][1]
