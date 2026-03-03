import sys

k, n = map(int, sys.stdin.readline().split())
a = []
for _ in range(k):
    a.append(int(sys.stdin.readline()))

low = 1
high = max(a)
answer = 0

while low <= high:
    mid = (low + high) // 2
    num_wires = sum(map(lambda x: x // mid, a))
    if num_wires < n:
        high = mid - 1
    else:
        answer = mid
        low = mid + 1

print(answer)
