class Node:
    def __init__(self, n):
        self.n = n
        self.cnt = -1
        self.conn = set()


def denode(nodes, node, cnt):
    if node.cnt != -1:
        return False

    node.cnt = cnt
    for i in node.conn:
        denode(nodes, nodes[i], cnt)

    return True


def solution(n, computers):
    nodes = [Node(i) for i in range(n)]

    for i in range(1, n):
        for j in range(0, i):
            if computers[i][j]:
                nodes[i].conn.add(j)
                nodes[j].conn.add(i)

    cnt = 0
    for i, node in enumerate(nodes):
        if denode(nodes, node, cnt):
            cnt += 1

    return cnt
