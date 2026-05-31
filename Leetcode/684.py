from typing import List

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

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = UnionFind(len(edges))
        redundant = []
        for edge in edges:
            a, b = edge[0], edge[1]
            pa, pb = graph.find(a), graph.find(b)
            if pa == pb:
                redundant.append([a, b])
            graph.union(a, b)
        return redundant[-1]
