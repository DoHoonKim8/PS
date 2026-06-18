from typing import List
from collections import deque

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        num_rows = len(grid)
        num_cols = len(grid[0])
        dist_upper_bound = num_rows * num_cols
        dist = [[[dist_upper_bound] * (k + 1) for _ in range(num_cols)] for _ in range(num_rows)]
        queue = deque()
        queue.append((0, 0, 0))
        dist[0][0][0] = 0
        delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while queue:
            x, y, num_obstacles_removed = queue.popleft()
            if x == num_rows - 1 and y == num_cols - 1:
                return dist[x][y][num_obstacles_removed]
            for dx, dy in delta:
                nx, ny = x + dx, y + dy
                if 0 <= nx < num_rows and 0 <= ny < num_cols:
                    if grid[nx][ny] == 0:
                        if dist[nx][ny][num_obstacles_removed] == dist_upper_bound:
                            dist[nx][ny][num_obstacles_removed] = dist[x][y][num_obstacles_removed] + 1
                            queue.append((nx, ny, num_obstacles_removed))
                    else:
                        if num_obstacles_removed + 1 <= k and dist[nx][ny][num_obstacles_removed + 1] == dist_upper_bound:
                            dist[nx][ny][num_obstacles_removed + 1] = dist[x][y][num_obstacles_removed] + 1
                            queue.append((nx, ny, num_obstacles_removed + 1))
        return -1
