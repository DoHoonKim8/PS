from collections import defaultdict
from typing import List
import heapq

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = defaultdict(list)
        for (u, v, w) in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
        min_num_cities = n
        answer = 0
        for city in range(n):
            rem_dist = [-1] * n
            rem_dist[city] = distanceThreshold
            heap = [(-distanceThreshold, city)]
            while heap:
                minus_curr_rem_dist, curr = heapq.heappop(heap)
                curr_rem_dist = -minus_curr_rem_dist
                if rem_dist[curr] > curr_rem_dist:
                    continue
                for (adj, dist) in graph[curr]:
                    if curr_rem_dist - dist >= 0 and rem_dist[adj] < curr_rem_dist - dist:
                        rem_dist[adj] = curr_rem_dist - dist
                        heapq.heappush(heap, (-rem_dist[adj], adj))
            num_cities = 0
            for dst in range(n):
                if dst == city:
                    continue
                if rem_dist[dst] >= 0:
                    num_cities += 1
            if num_cities <= min_num_cities:
                min_num_cities = num_cities
                answer = city
        return answer
