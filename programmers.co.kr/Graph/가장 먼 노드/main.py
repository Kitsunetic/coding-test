from queue import Queue
from collections import defaultdict


class Node:
    def __init__(self, n):
        self.n = n
        self.childs = []
        self.d = -1

    def add(self, v):
        self.childs.append(v)


def solution(n, vertex):
    nodelist = [Node(i) for i in range(n + 1)]

    for a, b in vertex:
        nodelist[a].add(b)
        nodelist[b].add(a)

    q = Queue()
    q.put((1, 0))
    x = defaultdict(bool)
    while not q.empty():
        v, d = q.get()
        if nodelist[v].d != -1:
            continue

        # print(v, d, nodelist[v].childs)
        nodelist[v].d = d

        for c in nodelist[v].childs:
            if not x[c]:
                q.put((c, d + 1))
                # print("x", c, d + 1)
                x[c] = True

    maxd, maxc = -1, 0
    for node in nodelist:
        if node.d > maxd:
            maxd = node.d
            maxc = 1
        elif node.d == maxd:
            maxc += 1

    return maxc
