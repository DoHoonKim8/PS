import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = [[0] * n for _ in range(n)]
for _ in range(m):
    order = list(map(int, sys.stdin.readline().split()))
    order.pop(0)
    for (s, d) in zip(order, order[1:]):
        graph[d - 1][s - 1] = 1

queue = deque()
visited = [False for _ in range(n)]
for d in range(1, n + 1):
    if sum(graph[d - 1]) == 0:
        queue.append(d)
        visited[d - 1] = True

answer = []
while len(queue) > 0:
    s = queue.popleft()
    answer.append(s)
    for d in range(1, n + 1):
        if not visited[d - 1]:
            graph[d - 1][s - 1] = 0
            if sum(graph[d - 1]) == 0:
                queue.append(d)
                visited[d - 1] = True

if len(answer) < n:
    print(0)
    exit(0)

print('\n'.join(map(str, answer)))
