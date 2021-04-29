from queue import Queue


def solution(n, results):
    mat = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        mat[i][i] = 1
    for a, b in results:
        mat[a][b] = 1

    for t in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if j == i or mat[i][j] == 0:
                    continue

                if mat[i][j] == 1:
                    for k in range(1, n + 1):
                        mat[k][j] |= mat[k][i]

    u = {i for i in range(1, n + 1)}
    cnt = 0

    for i in range(1, n + 1):
        s = set()
        for j in range(1, n + 1):
            if mat[i][j] == 1:
                s.add(j)
            if mat[j][i] == 1:
                s.add(j)

        if s == u:
            cnt += 1

    return cnt
