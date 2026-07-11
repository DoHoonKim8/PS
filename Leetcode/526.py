class Solution:
    def countArrangement(self, n: int) -> int:
        dp = [0] * (1 << n)
        dp[0] = 1
        for mask in range(1 << n):
            i = mask.bit_count()
            for j in range(n):
                if mask & (1 << j):
                    continue
                new_mask = mask | (1 << j)
                if (i + 1) % (j + 1) == 0 or (j + 1) % (i + 1) == 0:
                    dp[new_mask] += dp[mask]
        return dp[-1]
