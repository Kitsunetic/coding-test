alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphavets = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
alphanets = {v: i for i, v in zip(alphavets, alphabets)}


class Solver:
    def __init__(self, name):
        self.name = list(name)
        self.N = len(self.name)
        self.cursor = 0
        self.answer = 0

    def stand(self):
        self.answer += alphanets[self.name[self.cursor]]
        self.name[self.cursor] = "A"

    def see(self):
        name = self.name + self.name + self.name
        c = self.N + self.cursor

        # see left
        dl, zl = None, None
        for l in range(c - 1, -1, -1):
            if name[l] != "A":
                dl = c - l
                break
        if dl is not None:
            for i in range(l - 1, -1, -1):
                if name[i] == "A":
                    zl = c - i
                    break

        # see right
        dr, zr = None, None
        for r in range(c + 1, 3 * self.N, 1):
            if name[r] != "A":
                dr = r - c
                break
        if dr is not None:
            for i in range(r + 1, 3 * self.N, 1):
                if name[i] == "A":
                    zr = i - c
                    break

        return dl, zl, dr, zr

    def move(self, dl, zl, dr, zr):
        if dr is None or dl is None:
            return True
        elif dl > dr:
            self.cursor += dr
            if self.cursor >= self.N:
                self.cursor -= self.N
            self.answer += dr
        elif dl < dr:
            self.cursor -= dl
            if self.cursor < 0:
                self.cursor += self.N
            self.answer += dl
        elif zl < zr:
            self.cursor -= dl
            if self.cursor < 0:
                self.cursor += self.N
            self.answer += dl
        else:
            self.cursor += dr
            if self.cursor >= self.N:
                self.cursor -= self.N
            self.answer += dr

        return False

    def do(self):
        while True:
            self.stand()
            l, dl, r, dr = self.see()
            # print(self.cursor, l, dl, r, dr)
            if self.move(l, dl, r, dr):
                break


def solution(name):
    solver = Solver(name)
    solver.do()

    return solver.answer
