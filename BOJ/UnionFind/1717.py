class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.rank = [0] * (n + 1)

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return
        if self.rank[ra] < self.rank[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        if self.rank[ra] == self.rank[rb]:
            self.rank[ra] += 1

import sys

n, m = map(int, sys.stdin.readline().split())
tree = UnionFind(n)
answer = ''
for _ in range(m):
    op, a, b = map(int, sys.stdin.readline().split())
    if op == 0:
        tree.union(a, b)
    else:
        if tree.find(a) == tree.find(b):
            answer += 'YES\n'
        else:
            answer += 'NO\n'

print(answer)
