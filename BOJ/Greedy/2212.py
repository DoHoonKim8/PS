import sys

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
sensors = list(map(int, sys.stdin.readline().split()))

sensors.sort()
adj = []
for a, b in zip(sensors, sensors[1:]):
    adj.append(b - a)

adj.sort()
print(adj)
print(sum(adj[:n - k]))
