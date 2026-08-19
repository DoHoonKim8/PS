from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        left_max_height = 0
        left_max_height_arr = [left_max_height]
        for i in range(len(height)):
            left_max_height = max(left_max_height, height[i])
            left_max_height_arr.append(left_max_height)
        right_max_height = 0
        right_max_height_arr = [0] * len(height)
        for i in range(len(height) - 2, -1, -1):
            right_max_height = max(right_max_height, height[i + 1])
            right_max_height_arr[i] = right_max_height
        result = 0
        for i in range(len(height)):
            diff = min(right_max_height_arr[i], left_max_height_arr[i])
            result += max(diff - height[i], 0)
        return result
