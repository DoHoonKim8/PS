import sys
from collections import defaultdict, deque

# make DAG of components
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
dag = defaultdict(list)
indegree = [0] * (n + 1)
for _ in range(m):
    x, y, k = map(int, sys.stdin.readline().split())
    dag[y].append((x, k))
    indegree[x] += 1

# find basic components
basic_components = []
for i in range(1, n + 1):
    if indegree[i] == 0:
        basic_components.append(i)

# dp from basic to final
queue = deque()
for c in basic_components:
    queue.append(c)

dp = [dict(zip(basic_components, [0] * len(basic_components))) for _ in range(n + 1)]
for c in basic_components:
    dp[c][c] = 1
final = 0

while len(queue) > 0:
    curr = queue.popleft()
    if len(dag[curr]) == 0:
        final = curr
        break
    for adj, num in dag[curr]:
        indegree[adj] -= 1
        if indegree[adj] == 0:
            queue.append(adj)
        for b in dp[adj].keys():
            dp[adj][b] += num * dp[curr][b]

for k, v in dp[final].items():
    print(' '.join(map(str, [k, v])))
