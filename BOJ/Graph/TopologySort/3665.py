import sys
from collections import deque

num_tests = int(sys.stdin.readline())
for _ in range(num_tests):
    n = int(sys.stdin.readline())
    t = list(map(int, sys.stdin.readline().split()))
    indegree = [0] * (n + 1)

    graph = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    for i in range(len(t)):
        for j in range(len(t)):
            if i < j:
                graph[t[j]][t[i]] = 1
                indegree[t[i]] += 1

    m = int(sys.stdin.readline())
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        if graph[a][b] == 1:
            graph[a][b] = 0
            graph[b][a] = 1
            indegree[a] += 1
            indegree[b] -= 1
        elif graph[b][a] == 1:
            graph[b][a] = 0
            graph[a][b] = 1
            indegree[a] -= 1
            indegree[b] += 1
    queue = deque()
    for i in range(1, n + 1):
        if indegree[i] == 0:
            queue.append(i)
    answer = []
    while len(queue) > 0:
        if len(queue) > 1:
            print('?')
            exit(0)
        curr = queue.popleft()
        answer.append(curr)
        for i in range(1, n + 1):
            if graph[curr][i] == 1:
                indegree[i] -= 1
                if indegree[i] == 0:
                    queue.append(i)

    if len(queue) == 0 and len(answer) < n:
        print("IMPOSSIBLE")
    else:
        print(' '.join(map(str, reversed(answer))))
