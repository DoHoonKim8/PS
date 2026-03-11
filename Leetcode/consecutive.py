def longest_consecutive(nums: list[int]) -> int:
    if len(nums) == 0:
        return 0
    nums_set = set(nums)
    consecutive_len = 0
    longest_consecutive_len = 0
    for x in nums_set:
        if x - 1 not in nums_set:
            while x in nums_set:
                consecutive_len += 1
                x += 1
            longest_consecutive_len = max(longest_consecutive_len, consecutive_len)
            consecutive_len = 0
    
    return longest_consecutive_len

import sys

nums = list(map(int, sys.stdin.readline().split()))
print(longest_consecutive(nums))
