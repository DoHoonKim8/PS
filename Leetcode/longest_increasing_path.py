def dfs(grid, row, col, cache_longest):
    n, m = len(grid), len(grid[0])
    longest_child_path = 0
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = row + dr, col + dc
        if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] > grid[row][col]:
            if cache_longest[nr][nc] == 0:
                dfs(grid, nr, nc, cache_longest)
            longest_child_path = max(longest_child_path, cache_longest[nr][nc])
    cache_longest[row][col] = longest_child_path + 1

def longest_increasing_path(grid: list[list[int]]) -> int:
    n, m = len(grid), len(grid[0])
    cache_longest = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if cache_longest[i][j] == 0:
                dfs(grid, i, j, cache_longest)

    longest = 0
    for i in range(n):
        longest = max(longest, max(cache_longest[i]))

    return longest

print(longest_increasing_path([[3, 3, 3], [3, 3, 3]]))
