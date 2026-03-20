import sys
from collections import defaultdict
import heapq

n, m, k = map(int, sys.stdin.readline().split())
graph = defaultdict(list)
for _ in range(m):
    x, y, w = map(int, sys.stdin.readline().split())
    graph[x].append((y, w))
    graph[y].append((x, w))

heap = [(0, 1, 0)] # distance, node, the number of paved roads
dist = [[0] * (k + 1) for _ in range(n + 1)]
visited = set()

while heap:
    distance, node, num_paved = heapq.heappop(heap)
    if (node, num_paved) in visited:
        continue
    visited.add((node, num_paved))
    dist[node][num_paved] = distance
    for adj, weight in graph[node]:
        heapq.heappush(heap, (distance + weight, adj, num_paved))
        if num_paved < k:
            heapq.heappush(heap, (distance, adj, num_paved + 1))

print(min(dist[n]))
