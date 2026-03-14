import sys

def dfs(grid, row, col, visited):
    n, m = len(grid), len(grid[0])

    stack = [(row, col)]
    while stack:
        r, c = stack.pop()
        if visited[r][c]:
            continue
        visited[r][c] = True
        for (dr, dc) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 1 and not visited[nr][nc]:
                stack.append((nr, nc))

num_tests = int(sys.stdin.readline())
for _ in range(num_tests):
    m, n, k = map(int, sys.stdin.readline().split())
    grid = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    for _ in range(k):
        c, r = map(int, sys.stdin.readline().split())
        grid[r][c] = 1
    answer = 0
    for r in range(n):
        for c in range(m):
            if grid[r][c] == 1 and not visited[r][c]:
                dfs(grid, r, c, visited)
                answer += 1
    print(answer)
