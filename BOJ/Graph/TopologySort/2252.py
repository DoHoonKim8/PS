import sys
from collections import deque, defaultdict

n, m = map(int, sys.stdin.readline().split())
graph = defaultdict(list)
indegree = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    indegree[b] += 1

queue = deque()
for i in range(1, n + 1):
    if indegree[i] == 0:
        queue.append(i)

answer = []
while queue:
    node = queue.popleft()
    answer.append(node)
    for next in graph[node]:
        indegree[next] -= 1
        if indegree[next] == 0:
            queue.append(next)

print(' '.join(map(str, answer)))
