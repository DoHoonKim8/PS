import sys
from collections import deque

def solution():
    n, m = map(int, sys.stdin.readline().split())
    maze = [[0] * m for _ in range(n)]
    for i in range(n):
        line = input()
        maze[i] = list(map(int, line))

    dist = [[0] * m for _ in range(n)]

    dist[0][0] = 1
    queue = deque([(0, 0)])
    while queue:
        r, c = queue.popleft()
        for (dr, dc) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < m and dist[nr][nc] == 0 and maze[nr][nc] == 1:
                dist[nr][nc] = dist[r][c] + 1
                queue.append((nr, nc))
    return dist[n - 1][m - 1]

print(solution())
