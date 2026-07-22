from typing import List
import sys
import heapq

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n, m = len(moveTime), len(moveTime[0])
        dist = [[sys.maxsize for _ in range(m)] for _ in range(n)]
        heap = [(0, 0, 0)]
        delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while heap:
            curr, row, col = heapq.heappop(heap)
            if curr > dist[row][col]:
                continue
            if row == n - 1 and col == m - 1:
                return curr
            for dr, dc in delta:
                nr, nc = row + dr, col + dc
                if 0 <= nr < n and 0 <= nc < m:
                    to_new = max(moveTime[nr][nc], curr) + 1
                    if to_new < dist[nr][nc]:
                        dist[nr][nc] = to_new
                        heapq.heappush(heap, (to_new, nr, nc))
        return dist[-1][-1]
