from typing import List
from collections import deque
import string


class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        num_rows, num_cols = len(grid), len(grid[0])
        alphabet = set()
        start = (0, 0)
        for i in range(0, num_rows):
            for j in range(0, num_cols):
                if grid[i][j] == '@':
                    start = (i, j)
                if grid[i][j] in string.ascii_letters:
                    alphabet.add(grid[i][j].lower())
        k = len(alphabet)
        queue = deque()
        queue.append((start[0], start[1], 0, 0))
        visited = set([(start[0], start[1], 0)])
        delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while queue:
            row, col, dist, acquired_keys = queue.popleft()
            if acquired_keys == (1 << k) - 1:
                return dist
            for dr, dc in delta:
                nr, nc = row + dr, col + dc
                if 0 <= nr < num_rows and 0 <= nc < num_cols:
                    if (grid[nr][nc] == '.' or grid[nr][nc] == '@') and (nr, nc, acquired_keys) not in visited:
                        visited.add((nr, nc, acquired_keys))
                        queue.append((nr, nc, dist + 1, acquired_keys))
                    elif grid[nr][nc] in string.ascii_letters:
                        if grid[nr][nc] == grid[nr][nc].lower():
                            new_acquired_keys = acquired_keys | 1 << (ord(grid[nr][nc]) - ord('a'))
                            if (nr, nc, new_acquired_keys) not in visited:
                                visited.add((nr, nc, new_acquired_keys))
                                queue.append((nr, nc, dist + 1, new_acquired_keys))
                        elif acquired_keys & (1 << (ord(grid[nr][nc]) - ord('A'))) and (nr, nc, acquired_keys) not in visited:
                            visited.add((nr, nc, acquired_keys))
                            queue.append((nr, nc, dist + 1, acquired_keys))
        return -1
