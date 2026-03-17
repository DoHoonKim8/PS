import sys
from collections import defaultdict
import heapq

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph = defaultdict(list)
for _ in range(m):
    a, b, w = map(int, sys.stdin.readline().split())
    graph[a].append((b, w))

s, d = map(int, sys.stdin.readline().split())

dist = [sys.maxsize] * (n + 1)
dist[s] = 0
heap = [(0, s)]
visited = set([])
while heap:
    curr_dist, curr = heapq.heappop(heap)
    if curr in visited:
        continue
    visited.add(curr)
    dist[curr] = curr_dist
    for to, weight in graph[curr]:
        heapq.heappush(heap, (min(dist[to], curr_dist + weight), to))

print(dist[d])
