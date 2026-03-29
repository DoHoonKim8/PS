import sys

n, s = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

left, right = 0, 1
partial_sum = nums[0]
shortest = 1 if partial_sum >= s else n + 1
while 0 <= left < n and 0 < right <= n:
    if partial_sum < s:
        if right < n:
            partial_sum += nums[right]
            right += 1
        else:
            break
    else:
        shortest = min(shortest, right - left)
        partial_sum -= nums[left]
        left += 1

if shortest == n + 1:
    print(0)
else:
    print(shortest)
