import sys
from collections import deque, defaultdict

n, m = map(int, sys.stdin.readline().split())

graph = defaultdict(list)
indirect = [0] * (n + 1)
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    indirect[b] += 1

queue = deque()
semester = [-1] * (n + 1)
for d in range(1, len(indirect)):
    if indirect[d] == 0:
        queue.append(d)
        semester[d] = 1

while len(queue) > 0:
    s = queue.popleft()
    for d in graph[s]:
        indirect[d] -= 1
        if indirect[d] == 0:
            queue.append(d)
            semester[d] = semester[s] + 1

print(' '.join(map(str, semester[1:])))
