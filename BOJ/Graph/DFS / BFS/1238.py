import sys
from collections import defaultdict
import heapq

n, m, x = map(int, sys.stdin.readline().split())
graph = defaultdict(list)
reversed_graph = defaultdict(list)

for _ in range(m):
    a, b, t = map(int, sys.stdin.readline().split())
    graph[a].append((b, t))
    reversed_graph[b].append((a, t))

attend_time = [sys.maxsize] * (n + 1)
attend_time[x] = 0
heap = [(0, x)]
determined = set()
while heap:
    time_curr, curr = heapq.heappop(heap)
    if curr in determined:
        continue
    attend_time[curr] = time_curr
    determined.add(curr)
    for to, time_to in reversed_graph[curr]:
        heapq.heappush(heap, (time_curr + time_to, to))

return_time = [sys.maxsize] * (n + 1)
return_time[x] = 0
heap = [(0, x)]
determined = set()
while heap:
    time_curr, curr = heapq.heappop(heap)
    if curr in determined:
        continue
    return_time[curr] = time_curr
    determined.add(curr)
    for to, time_to in graph[curr]:
        heapq.heappush(heap, (time_curr + time_to, to))

print(max(map(lambda e: e[0] + e[1], zip(attend_time[1:], return_time[1:]))))
