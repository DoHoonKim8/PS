import sys
from collections import deque

m, n, h = map(int, sys.stdin.readline().split())
box = [[[0] * m for _ in range(n)] for _ in range(h)]

for z in range(h):
    for y in range(n):
        box[z][y] = list(map(int, sys.stdin.readline().split()))

queue = deque()
num_tomatoes = 0
num_pushs = 0
for z in range(h):
    for y in range(n):
        for x in range(m):
            if box[z][y][x] != -1:
                num_tomatoes += 1
            if box[z][y][x] == 1:
                queue.append((z, y, x, 0))
                num_pushs += 1

if len(queue) == num_tomatoes:
    print(0)
    exit(0)

num_days = 0
while len(queue) > 0:
    z, y, x, day = queue.popleft()
    for dz, dy, dx in [(-1, 0, 0), (0, -1, 0), (0, 0, -1), (1, 0, 0), (0, 1, 0), (0, 0, 1)]:
        nz, ny, nx = z + dz, y + dy, x + dx
        if 0 <= nz < h and 0 <= ny < n and 0 <= nx < m and box[nz][ny][nx] == 0:
            box[nz][ny][nx] = 1
            queue.append((nz, ny, nx, day + 1))
            num_pushs += 1
            num_days = day + 1

if num_pushs < num_tomatoes:
    print(-1)
else:
    print(num_days)
