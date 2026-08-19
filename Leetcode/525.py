from typing import List

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        balance = {0: 0}
        num_zeros = 0
        num_ones = 0
        longest_subarr_lens = []
        for end in range(1, len(nums) + 1):
            if nums[end - 1] == 0:
                num_zeros += 1
            else:
                num_ones += 1
            if (index := balance.get(num_zeros - num_ones)) is not None:
                longest_subarr_lens.append(end - index)
            else:
                balance[num_zeros - num_ones] = end
                longest_subarr_lens.append(0)
        return max(longest_subarr_lens)
