import sys

n, k = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

partial_sum = sum(nums[:k])
max_partial_sum = partial_sum
for i in range(k, n):
    partial_sum = partial_sum + nums[i] - nums[i - k]
    max_partial_sum = max(max_partial_sum, partial_sum)

print(max_partial_sum)
