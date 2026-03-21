import sys
from collections import defaultdict

sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline())
graph = defaultdict(list)
for _ in range(n - 1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(tree, visited, curr):
    visited.add(curr)
    num_adapters_with_curr = 1
    num_adapters_without_curr = 0
    for adj in tree[curr]:
        if adj not in visited:
            num_adapters_with_adj, num_adapters_without_adj = dfs(tree, visited, adj)
            num_adapters_with_curr += min(num_adapters_with_adj, num_adapters_without_adj)
            num_adapters_without_curr += num_adapters_with_adj
    return (num_adapters_with_curr, num_adapters_without_curr)

visited = set()
num_adapters = dfs(graph, visited, 1)
print(min(num_adapters[0], num_adapters[1]))
