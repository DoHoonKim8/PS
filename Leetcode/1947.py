from typing import List

class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        m = len(mentors)
        dp = [0] * (1 << m)
        for mask in range(1 << m):
            used_mentors = mask.bit_count()
            for new in range(m):
                if mask & (1 << new):
                    continue
                new_mask = mask | (1 << new)
                next_student = students[used_mentors]
                score = sum(map(lambda e: 1 if e[0] == e[1] else 0, zip(next_student, mentors[new])))
                dp[new_mask] = max(dp[new_mask], dp[mask] + score)
        return dp[-1]
