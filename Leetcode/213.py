class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return max(nums)
        dp0 = [0] * len(nums)
        dp1 = [0] * len(nums)
        dp0[0] = nums[0]
        dp0[1] = max(nums[0], nums[1])
        dp1[1] = nums[1]
        for i in range(2, len(nums) - 1):
            dp0[i] = max(nums[i] + dp0[i - 2], dp0[i - 1])
            dp1[i] = max(nums[i] + dp1[i - 2], dp1[i - 1])
        dp0[-1] = max(nums[-1] + dp1[len(nums) - 3], dp0[len(nums) - 2])
        return dp0[-1]
