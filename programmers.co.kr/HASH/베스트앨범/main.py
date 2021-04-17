# lv3
# https://programmers.co.kr/learn/courses/30/lessons/42579


class Genre:
    def __init__(self, genre):
        self.genre = genre
        self.score = 0
        self.max1 = (-1, 0)
        self.max2 = (-1, 0)

    def __call__(self, i, v):
        self.score += v

        a = self.max1[1] < v
        b = self.max2[1] < v

        if a and b:
            self.max2 = self.max1
            self.max1 = (i, v)
        elif a and not b:
            raise NotImplementedError()
        elif not a and b:
            self.max2 = (i, v)
        elif not a and not b:
            pass

    def __str__(self):
        return f"{self.score}: {self.max1}, {self.max2}"

    def __repr__(self):
        return str(self)


def solution(genres, plays):
    N = len(genres)

    pgens = {}
    for i in range(N):
        genre = genres[i]
        play = plays[i]

        if genre not in pgens:
            pgens[genre] = Genre(genre)
        pgens[genre](i, play)

    genre_order = sorted(pgens, key=lambda genre: pgens[genre].score, reverse=True)

    answer = []
    for genre in genre_order:
        pgen = pgens[genre]
        answer.append(pgen.max1[0])
        if pgen.max2[0] != -1:
            answer.append(pgen.max2[0])

    return answer
