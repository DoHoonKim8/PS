import sys
import heapq

n = int(sys.stdin.readline())
tasks = []
for _ in range(n):
    deadline, reward = map(int, sys.stdin.readline().split())
    tasks.append((deadline, reward))

tasks.sort()
heap = []
for deadline, reward in tasks:
    heapq.heappush(heap, reward)
    if len(heap) > deadline:
        heapq.heappop(heap)

print(sum(heap))
