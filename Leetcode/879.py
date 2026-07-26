from typing import List

class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        dp = [[0] * (n + 1) for _ in range(minProfit + 1)] # (profit, members)
        next_dp = [[0] * (n + 1) for _ in range(minProfit + 1)]
        dp[0][0] = 1
        for i in range(1, len(profit) + 1):
            for curr_profit in range(minProfit + 1):
                for curr_members in range(n + 1):
                    next_dp[curr_profit][curr_members] += dp[curr_profit][curr_members]
                    next_members = curr_members + group[i - 1]
                    if next_members > n:
                        continue
                    next_profit = min(minProfit, curr_profit + profit[i - 1])
                    next_dp[next_profit][next_members] += dp[curr_profit][curr_members]
            dp = next_dp
            if i < len(profit):
                next_dp = [[0] * (n + 1) for _ in range(minProfit + 1)]
        return sum(dp[minProfit]) % (1000000007)
