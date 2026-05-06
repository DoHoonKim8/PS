class Solution:
    def dfs(self, grid: List[List[str]], row: int, col: int, visited: set):
        n, m = len(grid), len(grid[0])
        stack = [(row, col)]

        while stack:
            r, c = stack.pop()
            if (r, c) in visited:
                continue
            visited.add((r, c))
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == '1' and not (nr, nc) in visited:
                    stack.append((nr, nc))

    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        visited = set()
        answer = 0
        for r in range(n):
            for c in range(m):
                if grid[r][c] == '1' and not (r, c) in visited:
                    self.dfs(grid, r, c, visited)
                    answer += 1
        return answer
