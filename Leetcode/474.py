from typing import List


class Solution:
    def numZerosOnes(self, binary: str) -> tuple[int, int]:
        zero, one = 0, 0
        for c in binary:
            if c == "0":
                zero += 1
            else:
                one += 1
        return zero, one

    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for s in strs:
            zeros, ones = self.numZerosOnes(s)
            prev = [row[:] for row in dp]

            for used_zero in range(m + 1):
                for used_one in range(n + 1):
                    if used_zero + zeros > m or used_one + ones > n:
                        continue

                    dp[used_zero + zeros][used_one + ones] = max(
                        dp[used_zero + zeros][used_one + ones],
                        prev[used_zero][used_one] + 1,
                    )

        return max(max(row) for row in dp)