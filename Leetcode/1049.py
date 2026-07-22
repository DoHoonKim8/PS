from typing import List

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        dp = [[False for _ in range(-3000, 3001)] for _ in range(1 + len(stones))]
        dp[0][3000] = True
        for i in range(1, 1 + len(stones)):
            for j in range(0, 6001):
                if dp[i - 1][j]:
                    dp[i][j + stones[i - 1]] = True
                    dp[i][j - stones[i - 1]] = True

        min_abs = 3001
        for i in range(0, 6001):
            if dp[-1][i]:
                if abs(i - 3000) < min_abs:
                    min_abs = abs(i - 3000)
        return min_abs
