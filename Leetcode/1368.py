from typing import List
import heapq

class Solution:
    def get_next_coord(self, direction, row, col, m, n) -> tuple[int, int] | None:
        result = (row, col)
        if direction == 1:
            result = (row, col + 1)
        elif direction == 2:
            result = (row, col - 1)
        elif direction == 3:
            result = (row + 1, col)
        elif direction == 4:
            result = (row - 1, col)
        if 0 <= result[0] < m and 0 <= result[1] < n:
            return result
        else:
            return None


    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        max_cost = m * n
        min_cost_dp = [[max_cost] * n for _ in range(m)]
        heap = [(0, (0, 0))]
        min_cost_dp[0][0] = 0
        while heap:
            curr_cost, coord = heapq.heappop(heap)
            row, col = coord
            if min_cost_dp[row][col] < curr_cost:
                continue
            if row == (m - 1) and col == (n - 1):
                return curr_cost
            if (next_coord := self.get_next_coord(grid[row][col], row, col, m, n)) is not None:
                next_row, next_col = next_coord
                next_cost = curr_cost
                if next_cost < min_cost_dp[next_row][next_col]:
                    min_cost_dp[next_row][next_col] = next_cost
                    heapq.heappush(heap, (next_cost, next_coord))
            for other_direction in ({1, 2, 3, 4} - {grid[row][col]}):
                if (next_coord := self.get_next_coord(other_direction, row, col, m, n)) is not None:
                    next_row, next_col = next_coord
                    next_cost = curr_cost + 1
                    if next_cost < min_cost_dp[next_row][next_col]:
                        min_cost_dp[next_row][next_col] = next_cost
                        heapq.heappush(heap, (next_cost, next_coord))
        return min_cost_dp[m - 1][n - 1]
