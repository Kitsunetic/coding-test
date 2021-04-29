def solution(numbers):
    P = []
    for n in numbers:
        n = str(n)
        P.append(((n * 4)[:4], n))

    Q = sorted(P, reverse=True)
    answer = str(int("".join(map(lambda x: x[1], Q))))  # 여기서 str(int())를 해야지 테스트11에서 통과함.
    return answer
