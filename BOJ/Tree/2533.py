import sys
from collections import defaultdict, deque

n = int(sys.stdin.readline())
graph = defaultdict(list)
for _ in range(n - 1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

queue = deque([1])
dist = [0] * (n + 1)
visited = set([1])
parent = [0] * (n + 1)
while queue:
    curr = queue.popleft()
    for adj in graph[curr]:
        if adj not in visited:
            dist[adj] = dist[curr] + 1
            queue.append(adj)
            visited.add(adj)
            parent[adj] = curr

tree = [[] for _ in range(n)]
for i in range(1, n + 1):
    tree[dist[i]].append(i)

adapter = set()
for height in range(len(tree) - 1, 0, -1):
    for node in tree[height]:
        if node not in adapter:
            adapter.add(parent[node])

print(len(adapter))
