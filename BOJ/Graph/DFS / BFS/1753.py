import sys
from collections import defaultdict
import heapq

v, e = map(int, sys.stdin.readline().split())
k = int(sys.stdin.readline())

graph = defaultdict(lambda: defaultdict(lambda: 11))
for _ in range(e):
    a, b, w = map(int, sys.stdin.readline().split())
    graph[a][b] = min(graph[a][b], w)

dist = [4000000] * (v + 1)
dist[k] = 0
edges = []
for adj, w in graph[k].items():
    edges.append((w, adj))
    dist[adj] = w

heapq.heapify(edges)

visited = set([k])

while edges:
    d, curr = heapq.heappop(edges)
    if curr in visited:
        continue
    visited.add(curr)
    dist[curr] = d
    for adj, w in graph[curr].items():
        dist[adj] = min(d + w, dist[adj])
        heapq.heappush(edges, (dist[adj], adj))

for i in range(1, v + 1):
    if dist[i] == 4000000:
        print('INF')
    else:
        print(dist[i])
