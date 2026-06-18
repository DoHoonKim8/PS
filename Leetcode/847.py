from typing import List
from collections import deque

class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        if n == 1 and len(graph[0]) == 0:
            return 0
        queue = deque()
        dist = [[0] * (1 << n) for _ in range(n)]
        visited = set()
        for i in range(n):
            queue.append((i, 1 << i))
        while queue:
            curr, visited_nodes = queue.popleft()
            for succ in graph[curr]:
                visited_nodes_succ = visited_nodes | (1 << succ)
                if (succ, visited_nodes_succ) not in visited:
                    visited.add((succ, visited_nodes_succ))
                    queue.append((succ, visited_nodes_succ))
                    dist[succ][visited_nodes_succ] = dist[curr][visited_nodes] + 1
                if visited_nodes_succ == ((1 << n) - 1):
                    return dist[succ][visited_nodes_succ]
