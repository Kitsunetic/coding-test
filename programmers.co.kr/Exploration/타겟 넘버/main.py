from queue import Queue


def solution(numbers, target):
    Q = Queue()
    Q.put((0, 0, 1))
    Q.put((0, 0, -1))

    cnt = 0
    while not Q.empty():
        c, i, s = Q.get()
        c += s * numbers[i]
        fv = sum(numbers[i + 1 :])

        if i == len(numbers) - 1:
            if c == target:
                cnt += 1
        else:
            if (c < target and c + fv < target) or (c > target and c - fv > target):
                continue
            # 여기 조건을 없애면 테스트1에서 7452ms, 있으면 2896ms가 걸린다. 어짼든 둘 다 통과

            Q.put((c, i + 1, 1))
            Q.put((c, i + 1, -1))

    return cnt
