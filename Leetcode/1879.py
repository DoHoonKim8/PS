from typing import List

class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        INF = 10**18
        dp = [INF] * (1 << n)
        dp[0] = 0
        for mask in range(0, 1 << n):
            num_selected = mask.bit_count()
            for j in range(n):
                if mask & (1 << j):
                    continue
                new_mask = mask | (1 << j)
                dp[new_mask] = min(dp[new_mask], dp[mask] + (nums1[num_selected] ^ nums2[j]))
        return dp[(1 << n) - 1]
