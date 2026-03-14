import sys

n = int(sys.stdin.readline())
num_edges = int(sys.stdin.readline())

graph = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(num_edges):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = 1
    graph[b][a] = 1

visited = [False] * (n + 1)
stack = [1]
answer = 0
while stack:
    curr = stack.pop()
    if visited[curr]:
        continue
    visited[curr] = True
    answer += 1
    for next in range(1, n + 1):
        if graph[curr][next] == 1 and not visited[next]:
            stack.append(next)

print(answer - 1)
