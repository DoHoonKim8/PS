from collections import defaultdict
from typing import List
import heapq, sys

class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for (u, v, w) in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
        heap = [(0, n)]
        distanceToLastNode = [sys.maxsize] * (n + 1)
        distanceToLastNode[n] = 0
        while heap:
            curr_dist, curr = heapq.heappop(heap)
            if distanceToLastNode[curr] < curr_dist:
                continue
            for (adj, dist) in graph[curr]:
                if distanceToLastNode[adj] > curr_dist + dist:
                    distanceToLastNode[adj] = curr_dist + dist
                    heapq.heappush(heap, (distanceToLastNode[adj], adj))
        maxHeap = [(-distanceToLastNode[1], 1)]
        pushed = set([1])
        num_restricted_paths = [0] * (n + 1)
        num_restricted_paths[1] = 1
        while maxHeap:
            _, curr = heapq.heappop(maxHeap)
            if curr == n:
                return num_restricted_paths[n]
            for adj, _ in graph[curr]:
                if distanceToLastNode[adj] < distanceToLastNode[curr]:
                    num_restricted_paths[adj] = (num_restricted_paths[adj] + num_restricted_paths[curr]) % (10**9 + 7)
                    if adj not in pushed:
                        heapq.heappush(maxHeap, (-distanceToLastNode[adj], adj))
                        pushed.add(adj)
        return num_restricted_paths[n] % (10**9 + 7)
