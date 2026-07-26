from collections import defaultdict
from typing import List
import heapq
import sys

class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        graph = defaultdict(list)
        for edge in edges:
            a, b = edge[0], edge[1]
            graph[a].append(b)
            graph[b].append(a)
        minimum = [sys.maxsize] * (n + 1)
        second_minimum = [sys.maxsize] * (n + 1)
        heap = [(0, 1)]
        minimum[1] = 0
        while heap:
            curr_time, curr = heapq.heappop(heap)
            if curr_time > second_minimum[curr]:
                continue
            waiting_time = 0 if curr_time % (2 * change) < change else change - (curr_time % change)
            next_time = curr_time + waiting_time + time
            for adj in graph[curr]:
                if next_time < minimum[adj]:
                    second_minimum[adj] = minimum[adj]
                    minimum[adj] = next_time
                    heapq.heappush(heap, (next_time, adj))
                if next_time > minimum[adj] and next_time < second_minimum[adj]:
                    second_minimum[adj] = next_time
                    heapq.heappush(heap, (next_time, adj))
        return second_minimum[n]
