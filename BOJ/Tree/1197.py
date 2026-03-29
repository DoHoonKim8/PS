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
import heapq

v, e = map(int, sys.stdin.readline().split())
tree = UnionFind(v)
edges = []
for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    heapq.heappush(edges, (c, a, b))

count = 0
weight = 0
while count < v - 1:
    c, a, b = heapq.heappop(edges)
    if tree.find(a) == tree.find(b):
        continue
    tree.union(a, b)
    count += 1
    weight += c

print(weight)
