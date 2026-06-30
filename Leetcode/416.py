from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        half = total // 2
        dp = [False for _ in range(total + 1)]
        dp[0] = True
        for i in range(len(nums)):
            new_sums = set()
            for j in range(half):
                if dp[j] is False:
                    continue
                new_sums.add(j + nums[i])
            for new_sum in new_sums:
                dp[new_sum] = True
        return dp[half]
