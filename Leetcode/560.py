from typing import List
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum_count = defaultdict(int)
        end_prefix_sum = 0
        count = 0
        for end in range(len(nums)):
            start_prefix_sum = end_prefix_sum + nums[end] - k
            prefix_sum_count[end_prefix_sum] += 1
            count += prefix_sum_count[start_prefix_sum]
            end_prefix_sum += nums[end]
        return count
