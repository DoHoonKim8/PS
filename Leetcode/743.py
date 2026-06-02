from typing import List
from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for t in times:
            u, v, w = t[0], t[1], t[2]
            graph[u].append((v, w))
        arrive_times = [10000] * (n + 1)
        heap = [(0, k)]
        count = 0
        min_travel_time = 0
        while heap:
            curr_time, curr = heapq.heappop(heap)
            if arrive_times[curr] <= curr_time:
                continue
            arrive_times[curr] = curr_time
            min_travel_time = curr_time
            count += 1
            for (succ, travel_time) in graph[curr]:
                heapq.heappush(heap, (curr_time + travel_time, succ))
        if count < n:
            return -1
        return min_travel_time
