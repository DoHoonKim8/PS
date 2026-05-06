class Solution:
    def rob_linear(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        dp = [0] * len(nums)
        dp[0], dp[1] = nums[0], max(nums[:2])
        for i in range(2, len(nums)):
            dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
        return dp[-1]

    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return max(nums)
        max_from_0_to_before_last = self.rob_linear(nums[:-1])
        max_from_1_to_before_before_last = self.rob_linear(nums[1:-2])
        return max(nums[-1] + max_from_1_to_before_before_last, max_from_0_to_before_last)
