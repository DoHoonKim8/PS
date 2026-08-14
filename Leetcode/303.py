from typing import List

class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = [0]
        prefix_sum = 0
        for i in range(len(nums)):
            prefix_sum += nums[i]
            self.prefix.append(prefix_sum)


    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right + 1] - self.prefix[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)