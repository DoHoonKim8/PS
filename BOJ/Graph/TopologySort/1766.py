import sys
from collections import defaultdict
import heapq

n, m = map(int, sys.stdin.readline().split())
graph = defaultdict(list)
indegree = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    indegree[b] += 1

problems = []
for i in range(1, n + 1):
    if indegree[i] == 0:
        heapq.heappush(problems, i)

answer = []
while problems:
    curr = heapq.heappop(problems)
    answer.append(curr)
    for next in graph[curr]:
        indegree[next] -= 1
        if indegree[next] == 0:
            heapq.heappush(problems, next)

print(' '.join(map(str, answer)))
