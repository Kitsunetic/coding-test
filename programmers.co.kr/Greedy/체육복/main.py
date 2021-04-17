def solution(n, lost, reserve):
    p = [1 for _ in range(n + 1)]
    for i in lost:
        p[i] -= 1
    for i in reserve:
        p[i] += 1

    for i in range(1, n + 1):
        if p[i] == 0:
            if i != 1 and p[i - 1] > 1:
                p[i] += 1
                p[i - 1] -= 1
            elif i != n and p[i + 1] > 1:
                p[i] += 1
                p[i + 1] -= 1

    answer = 0
    for v in p[1:]:
        answer += min(v, 1)

    return answer