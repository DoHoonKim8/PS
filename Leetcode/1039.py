from typing import List
import operator

class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        num_vertices = len(values)
        dp = [[48000000] * len(values) for _ in range(len(values))]
        for start in range(len(values)):
            dp[start][(start + 1) % len(values)] = 0
        for num in range(3, len(values) + 1):
            for start in range(len(values)):
                vertices = [(start + n) % num_vertices for n in range(num)]
                end = vertices[-1]
                for v in vertices[1:-1]:
                    dp[start][end] = min(dp[start][end], dp[start][v] + dp[v][end] + values[start] * values[end] * values[v])
        return dp[0][len(values) - 1]
