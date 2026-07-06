from typing import List

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp = [(1, 1)] * len(nums) # (length of the LIS that has i-th element as the last element, # of LIS)
        max_len = 1
        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[j] < nums[i]:
                    if dp[i][0] <= dp[j][0]:
                        dp[i] = (dp[j][0] + 1, dp[j][1])
                    elif dp[i][0] == dp[j][0] + 1:
                        dp[i] = (dp[i][0], dp[i][1] + dp[j][1])
            max_len = max(max_len, dp[i][0])
        total = 0
        for length, count in dp:
            if length == max_len:
                total += count
        return total
