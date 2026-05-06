from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        num_fresh = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    num_fresh += 1
                if grid[i][j] == 2:
                    queue.append((i, j, 0))

        max_time = 0
        while queue:
            row, col, time = queue.popleft()
            max_time = time
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = row + dr, col + dc
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 1:
                    num_fresh -= 1
                    grid[nr][nc] = 2
                    queue.append((nr, nc, time + 1))
        
        if num_fresh > 0:
            return -1
        else:
            return max_time