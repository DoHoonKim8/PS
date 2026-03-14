import sys
sys.setrecursionlimit(10**6)

m, n = map(int, sys.stdin.readline().split())
grid = [[0] * n for _ in range(m)]

for i in range(m):
    grid[i] = list(map(int, sys.stdin.readline().split()))

def dfs(grid, row, col, dp):
    m, n = len(grid), len(grid[0])

    num_paths = 0
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = row + dr, col + dc
        if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] < grid[row][col]:
            if dp[nr][nc] == -1:
                num_paths += dfs(grid, nr, nc, dp)
            else:
                num_paths += dp[nr][nc]

    dp[row][col] = num_paths
    return num_paths

dp = [[-1] * n for _ in range(m)]
dp[m - 1][n - 1] = 1
print(dfs(grid, 0, 0, dp))
