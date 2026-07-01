from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = [[0] * 2001 for _ in range(len(nums))] # the index of target = target + 1000
        dp[0][nums[0] + 1000] += 1
        dp[0][-nums[0] + 1000] += 1
        for i in range(1, len(nums)):
            for sub in range(-1000, 1001, 1):
                count = dp[i - 1][sub + 1000]
                if count > 0:
                    dp[i][sub + nums[i] + 1000] += count
                    dp[i][sub - nums[i] + 1000] += count
        return dp[-1][target + 1000]
