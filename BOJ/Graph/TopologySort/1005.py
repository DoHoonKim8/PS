import sys
from collections import defaultdict, deque

t = int(sys.stdin.readline())
for _ in range(t):
    n, k = map(int, sys.stdin.readline().split())
    construction_times = list(map(int, sys.stdin.readline().split()))
    graph = defaultdict(list)
    indegree = [0] * (n + 1)
    elapsed_times = [0] * (n + 1)
    for _ in range(k):
        x, y = map(int, sys.stdin.readline().split())
        graph[x].append(y)
        indegree[y] += 1

    w = int(sys.stdin.readline())
    queue = deque()
    for i in range(1, n + 1):
        if indegree[i] == 0:
            queue.append(i)
    while queue:
        curr = queue.popleft()
        elapsed_times[curr] += construction_times[curr - 1]
        for next_building in graph[curr]:
            indegree[next_building] -= 1
            elapsed_times[next_building] = max(elapsed_times[next_building], elapsed_times[curr])
            if indegree[next_building] == 0:
                queue.append(next_building)

    print(elapsed_times[w])
