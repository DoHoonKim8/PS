from typing import List

class Solution:
    def dfs(self, grid: List[List[int]], row, col, visited) -> int:
        num_rows = len(grid)
        num_cols = len(grid[0])
        stack = [(row, col)]
        visited.add((row, col))
        area = 1
        while stack:
            r, c = stack.pop()
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < num_rows and 0 <= nc < num_cols and grid[nr][nc] == 1 and not (nr, nc) in visited:
                    stack.append((nr, nc))
                    visited.add((nr, nc))
                    area += 1
        return area

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        max_area = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1 and not (row, col) in visited:
                    max_area = max(max_area, self.dfs(grid, row, col, visited))
        return max_area
