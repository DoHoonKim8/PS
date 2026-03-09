import sys
from collections import defaultdict, deque

n = int(sys.stdin.readline())

tree = defaultdict(list)

for _ in range(n - 1):
    a, b = map(int, sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)

parents = [-1] * (n + 1)
parents[1] = 0
queue = deque([(1, tree[1])])

while queue:
    parent, children = queue.popleft()
    for c in children:
        if parents[c] == -1:
            parents[c] = parent
            queue.append((c, tree[c]))

for i in range(2, n + 1):
    print(parents[i])
