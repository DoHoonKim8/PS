import sys
from collections import defaultdict

sys.setrecursionlimit(10**5)

n = int(sys.stdin.readline())
num_people = list(map(int, sys.stdin.readline().split()))
graph = defaultdict(list)
for _ in range(n - 1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(tree, root, visited):
    visited.add(root)
    root_is_good = num_people[root - 1]
    root_is_not_good = 0
    for adj in tree[root]:
        if adj not in visited:
            adj_is_good, adj_is_not_good = dfs(tree, adj, visited)
            root_is_good += adj_is_not_good
            root_is_not_good += max(adj_is_good, adj_is_not_good)

    return (root_is_good, root_is_not_good)

visited = set()
print(max(dfs(graph, 1, visited)))
