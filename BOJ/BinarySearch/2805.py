import sys

n, m = map(int, sys.stdin.readline().split())
heights = list(map(int, sys.stdin.readline().split()))

low = 1
high = max(heights)
answer = 0

while low <= high:
    mid = (low + high) // 2
    take = sum(map(lambda h: h - mid if h >= mid else 0, heights))
    if take >= m:
        answer = mid
        low = mid + 1
    else:
        high = mid - 1

print(answer)
