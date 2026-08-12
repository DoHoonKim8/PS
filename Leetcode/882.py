from collections import defaultdict
from typing import List
import heapq

class Solution:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        graph = defaultdict(list)
        for (u, v, cnt) in edges:
            graph[u].append((v, cnt + 1))
            graph[v].append((u, cnt + 1))
        remaining_dist = [-1] * n
        remaining_dist[0] = maxMoves
        heap = [(-maxMoves, 0)]
        while heap:
            minus_curr_rem_dist, curr = heapq.heappop(heap)
            curr_rem_dist = -minus_curr_rem_dist
            if remaining_dist[curr] > curr_rem_dist:
                continue
            for (adj, dist) in graph[curr]:
                if curr_rem_dist - dist < 0:
                    continue
                if curr_rem_dist - dist > remaining_dist[adj]:
                    remaining_dist[adj] = curr_rem_dist - dist
                    heapq.heappush(heap, (-remaining_dist[adj], adj))
        result = 0
        for (u, v, cnt) in edges:
            nums = 0
            if remaining_dist[u] != -1:
                nums += remaining_dist[u]
            if remaining_dist[v] != -1:
                nums += remaining_dist[v]
            result += min(cnt, nums)
        for node in range(n):
            if remaining_dist[node] != -1:
                result += 1
        return result
