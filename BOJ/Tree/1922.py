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
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
costs = []
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    costs.append((a, b, c))

costs.sort(key=lambda x: x[2])
tree = UnionFind(n)
count = 0
total_cost = 0
for a, b, c in costs:
    if tree.find(a) == tree.find(b):
        continue
    tree.union(a, b)
    count += 1
    total_cost += c

print(total_cost)
