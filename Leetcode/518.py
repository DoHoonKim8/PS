from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0] * (amount + 1) for _ in range(len(coins))]
        for i in range(amount + 1):
            if i * coins[0] > amount:
                break
            dp[0][i * coins[0]] = 1
        for row in range(1, len(coins)):
            dp[row][0] = 1
            for col in range(1, amount + 1):
                dp[row][col] = dp[row - 1][col]
                if col - coins[row] >= 0:
                    dp[row][col] += dp[row][col - coins[row]]
        return dp[-1][amount]
