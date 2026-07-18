from typing import List

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False
        target = total // k
        dp = [False] * (1 << len(nums))
        dp[0] = True
        for mask in range(1 << len(nums)):
            if not dp[mask]:
                continue
            subsum = 0
            for i in range(mask.bit_length()):
                if mask & (1 << i):
                    subsum += nums[i]
            bucket = subsum % target
            for i in range(len(nums)):
                if mask & (1 << i) or nums[i] > (target - bucket):
                    continue
                if dp[mask] and nums[i] <= (target - bucket):
                    new_mask = mask | (1 << i)
                    dp[new_mask] = True
        return dp[-1]
