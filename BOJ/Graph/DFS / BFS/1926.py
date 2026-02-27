import sys

def dfs(paper, i, j, visited, picture):
    col_len = len(paper)
    row_len = len(paper[0])
    stack = [(i, j)]
    while stack:
        row, col = stack.pop()
        if (row, col) in visited:
            continue
        visited.add((row, col))
        picture.append((row, col))
        for (dr, dc) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = row + dr, col + dc
            if 0 <= nr < col_len and 0 <= nc < row_len and (nr, nc) not in visited and paper[nr][nc] == 1:
                stack.append((nr, nc))

def solution():
    n, m = map(int, sys.stdin.readline().split())
    paper = [[0] * m for _ in range(n)]
    for i in range(n):
        line = list(map(int, sys.stdin.readline().split()))
        paper[i] = line

    visited = set()
    sizes = []
    for i in range(n):
        for j in range(m):
            if paper[i][j] == 1 and (i, j) not in visited:
                picture = []
                dfs(paper, i, j, visited, picture)
                sizes.append(len(picture))

    if len(sizes) == 0:
        return 0, 0
    else:
        return len(sizes), max(sizes)


num_pics, max_size = solution()
print(num_pics)
print(max_size)
