import sys
import math

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())

low = 1
high = n ** 2

answer = 0

while low <= high:
    mid = (low + high) // 2
    count = 0
    for row in range(1, n + 1):
        count += min(n, mid // row)
    if count < k:
        low = mid + 1
    else:
        answer = mid
        high = mid - 1

print(answer)
