import sys
from collections import deque

n, l = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

window = deque()
window.append((nums[0], 0))
sys.stdout.write(str(window[0][0]) + ' ')
for i in range(1, len(nums)):
    if i >= l and window[0][1] <= i - l:
        window.popleft()
    while len(window) > 0 and window[-1][0] > nums[i]:
        window.pop()
    window.append((nums[i], i))
    sys.stdout.write(str(window[0][0]) + ' ')
