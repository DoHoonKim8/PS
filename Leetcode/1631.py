from typing import List
import heapq

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        num_rows, num_cols = len(heights), len(heights[0])
        heap = [(0, 0, 0)]
        efforts = [[10**6] * num_cols for _ in range(num_rows)]
        while heap:
            effort, row, col = heapq.heappop(heap)
            if efforts[row][col] < 10**6:
                continue
            efforts[row][col] = effort
            for (dr, dc) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = row + dr, col + dc
                if 0 <= nr < num_rows and 0 <= nc < num_cols:
                    heapq.heappush(heap, (max(abs(heights[nr][nc] - heights[row][col]), effort), nr, nc))
        return efforts[num_rows - 1][num_cols - 1]
