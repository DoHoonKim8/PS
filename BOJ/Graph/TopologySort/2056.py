from collections import deque, defaultdict

def min_completion_time(n: int, tasks: list[tuple[int, list[int]]]) -> int:
    graph = defaultdict(list)
    completion_times = [0] * (n + 1)
    indegree = [0] * (n + 1)
    times = [0] * (n + 1)
    for i, (time, precedings) in enumerate(tasks, start=1):
        for pre in precedings:
            graph[pre].append(i)
        indegree[i] += len(precedings)
        times[i] = time

    queue = deque()
    for i in range(1, n + 1):
        if indegree[i] == 0:
            queue.append(i)

    while queue:
        curr = queue.popleft()
        completion_times[curr] += times[curr]
        for succ in graph[curr]:
            completion_times[succ] = max(completion_times[succ], completion_times[curr])
            indegree[succ] -= 1
            if indegree[succ] == 0:
                queue.append(succ)

    return max(completion_times)

import sys

n = int(sys.stdin.readline())
jobs = [(0, [])] * (n + 1)
for i in range(1, n + 1):
    inputs = list(map(int, sys.stdin.readline().split()))
    time = inputs[0]
    precs = inputs[2:]
    jobs[i] = (time, precs)

print(min_completion_time(n, jobs[1:]))
