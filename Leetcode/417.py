from typing import List

class Solution:
    def dfs(self, heights, row, col, visited) -> set:
        num_rows, num_cols = len(heights), len(heights[0])
        stack = [(row, col)]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        grids = set()
        grids.add((row, col))
        while stack:
            r, c = stack.pop()
            if (r, c) in visited:
                continue
            visited.add((r, c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < num_rows and 0 <= nc < num_cols and heights[nr][nc] >= heights[r][c] and (nr, nc) not in visited:
                    stack.append((nr, nc))
                    grids.add((nr, nc))
        return grids


    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        result = []
        pacific = set()
        atlantic = set()
        visited_from_pacific = set()
        visited_from_atlantic = set()
        for row in range(len(heights)):
            pacific = pacific.union(self.dfs(heights, row, 0, visited_from_pacific))
        for col in range(len(heights[0])):
            pacific = pacific.union(self.dfs(heights, 0, col, visited_from_pacific))

        for row in range(len(heights)):
            atlantic = atlantic.union(self.dfs(heights, row, len(heights[0]) - 1, visited_from_atlantic))

        for col in range(len(heights[0])):
            atlantic = atlantic.union(self.dfs(heights, len(heights) - 1, col, visited_from_atlantic))

        for row, col in pacific.intersection(atlantic):
            result.append([row, col])
        return result
