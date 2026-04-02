from bisect import bisect_right

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = list(zip(startTime, endTime, profit))
        jobs.sort(key=lambda x: x[1])
        num_jobs = len(jobs)
        starts = [jobs[i][0] for i in range(num_jobs)]
        profits = [jobs[i][2] for i in range(num_jobs)]
        ends = [jobs[i][1] for i in range(num_jobs)]
        dp = [0] * num_jobs
        dp[0] = profits[0]
        for i in range(1, num_jobs):
            prev = bisect_right(ends, starts[i])
            max_profit_with_i = profits[i]
            if prev > 0:
                max_profit_with_i += dp[prev - 1]
            dp[i] = max(dp[i - 1], max_profit_with_i)

        return dp[num_jobs - 1]
