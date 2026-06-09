from typing import Dict, List, Tuple

class Solution:
    dp: Dict[Tuple[int, int], int] = {}

    def maxCoins(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        nums = [1] + nums + [1]
        for l in range(1, len(nums)):
            for i in range(0, len(nums) - l):
                if l == 1:
                    self.dp[(i, i + l)] = 0
                elif l == 2:
                    self.dp[(i, i + l)] = nums[i] * nums[i + 1] * nums[i + 2]
                else:
                    self.dp[(i, i + l)] = 0
                    for k in range(i + 1, i + l):
                        self.dp[(i, i + l)] = max(self.dp[(i, i + l)], self.dp[(i, k)] + self.dp[(k, i + l)] + nums[i] * nums[k] * nums[i + l])
        return self.dp[(0, len(nums) - 1)]
