import sys
from bisect import bisect_left, bisect_right

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
b = list(map(int, sys.stdin.readline().split()))

a.sort()
answer = []
for i in range(m):
    answer.append(bisect_right(a, b[i]) - bisect_left(a, b[i]))

print(" ".join(map(str, answer)))
