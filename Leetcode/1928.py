from collections import defaultdict
from typing import List
import heapq, sys

class Solution:
    def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:
        graph = defaultdict(list)
        for x, y, time in edges:
            graph[x].append((y, time))
            graph[y].append((x, time))
        num_cities = len(passingFees)
        dp = [[sys.maxsize] * (maxTime + 1) for _ in range(num_cities)]
        dp[0][0] = passingFees[0]
        heap = [(passingFees[0], 0, 0)]
        while heap:
            curr_fee, curr_city, curr_time = heapq.heappop(heap)
            if dp[curr_city][curr_time] < curr_fee:
                continue
            for adj, time in graph[curr_city]:
                next_time = curr_time + time
                next_fee = curr_fee + passingFees[adj]
                if next_time > maxTime:
                    continue
                if dp[adj][next_time] > next_fee:
                    dp[adj][next_time] = next_fee
                    heapq.heappush(heap, (next_fee, adj, next_time))
        min_dst = min(dp[-1])
        result = min_dst if min_dst < sys.maxsize else -1
        return result
