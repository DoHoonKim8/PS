from typing import List
from collections import defaultdict
import heapq
import sys

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        for (u, v, time) in roads:
            graph[u].append((v, time))
            graph[v].append((u, time))
        shortest_times = [sys.maxsize] * n
        heap = [(0, 0)]
        ways = [0] * n
        ways[0] = 1
        while heap:
            curr_time, curr = heapq.heappop(heap)
            if curr_time > shortest_times[curr]:
                continue
            shortest_times[curr] = curr_time
            for succ, time in graph[curr]:
                if curr_time + time < shortest_times[succ]:
                    shortest_times[succ] = curr_time + time
                    ways[succ] = ways[curr]
                    heapq.heappush(heap, (curr_time + time, succ))
                elif curr_time + time == shortest_times[succ]:
                    ways[succ] += ways[curr]
        return ways[n - 1] % (10**9 + 7)
