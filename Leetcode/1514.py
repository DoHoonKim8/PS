from typing import List
from collections import defaultdict
import heapq

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)
        for (a, b), prob in zip(edges, succProb):
            graph[a].append((b, prob))
            graph[b].append((a, prob))
        probs = [0.0] * n
        heap = [(-1.0, start_node)]
        while heap:
            neg_curr_prob, curr = heapq.heappop(heap)
            curr_prob = -1.0 * neg_curr_prob
            if probs[curr] > curr_prob:
                continue
            probs[curr] = curr_prob
            for succ, to_succ_prob in graph[curr]:
                if probs[succ] < neg_curr_prob * to_succ_prob:
                    heapq.heappush(heap, (neg_curr_prob * to_succ_prob, succ))
        return probs[end_node]
