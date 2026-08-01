from typing import List

class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.sort()
        final_lens = [cuts[0]]
        for i in range(1, len(cuts)):
            final_lens.append(cuts[i] - cuts[i - 1])
        final_lens.append(n - cuts[-1])
        dp = [[0] * len(final_lens) for _ in range(len(final_lens))]
        for i in range(len(final_lens)):
            dp[i][i] = 0
        for num_parts in range(2, len(final_lens) + 1):
            for start in range(len(final_lens) - num_parts + 1):
                end = start + num_parts - 1
                total_len = 0
                for idx in range(start, end + 1):
                    total_len += final_lens[idx]
                if num_parts == 2:
                    dp[start][end] = total_len
                    continue
                min_sub_cut_cost = sys.maxsize
                for sep in range(start, end):
                    min_sub_cut_cost = min(min_sub_cut_cost, dp[start][sep] + dp[sep + 1][end])
                dp[start][end] = min_sub_cut_cost + total_len
        return dp[0][-1]
