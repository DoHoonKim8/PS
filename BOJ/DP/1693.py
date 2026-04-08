import sys
from collections import defaultdict

sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline())
tree = defaultdict(list)
for _ in range(n - 1):
    a, b = map(int, sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)

def find_first_and_second_min(array):
    first = sys.maxsize
    second = sys.maxsize
    for elem in array:
        if elem < first:
            second = first
            first = elem
        elif first <= elem and elem < second:
            second = elem
        else:
            continue
    return (first, second)

def dfs(tree, node, visited):
    visited.add(node)
    children_costs = []
    for adj in tree[node]:
        if adj not in visited:
            children_costs.append(dfs(tree, adj, visited))
    if len(children_costs) == 0:
        return [i for i in range(1, 20)]

    node_cost = [i for i in range(1, 20)]
    for i in range(1, 20):
        for child_cost in children_costs:
            first, second = find_first_and_second_min(child_cost)
            if child_cost[i - 1] == first:
                node_cost[i - 1] += second
            else:
                node_cost[i - 1] += first
    return node_cost

visited = set()

res = dfs(tree, 1, visited)
print(min(res))
