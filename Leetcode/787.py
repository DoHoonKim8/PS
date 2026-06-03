from typing import List
import sys

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        costs = [sys.maxsize] * n
        costs[src] = 0
        for _ in range(k + 1):
            next_costs = costs[:]
            for fr, to, price in flights:
                if costs[fr] != sys.maxsize:
                    next_costs[to] = min(next_costs[to], costs[fr] + price)
            costs = next_costs
        if costs[dst] < sys.maxsize:
            return costs[dst]
        else:
            return -1
