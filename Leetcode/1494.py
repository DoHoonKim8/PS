from typing import List
from collections import defaultdict
from itertools import combinations

class Solution:
    def getMask(self, courses: List[int]) -> int:
        mask = 0
        for course in courses:
            mask |= (1 << course)
        return mask

    def getCourses(self, mask: int, n: int) -> List[int]:
        courses = []
        for i in range(n):
            if mask & (1 << i):
                courses.append(i)
        return courses

    def minNumberOfSemesters(self, n: int, relations: List[List[int]], k: int) -> int:
        graph = defaultdict(list)
        indegree = [0] * n
        for prev_course, next_course in relations:
            graph[prev_course - 1].append(next_course - 1)
            indegree[next_course - 1] += 1
        MAX = n + 1
        dp = [MAX] * (1 << n)
        dp[0] = 0
        for mask in range(1 << n):
            if dp[mask] == MAX:
                continue
            taken = set(self.getCourses(mask, n))
            indegree_temp = indegree.copy()
            for c in taken:
                for c_adj in graph[c]:
                    indegree_temp[c_adj] -= 1
            available = []
            for c in range(n):
                if indegree_temp[c] == 0 and c not in taken:
                    available.append(c)
            if len(available) <= k:
                new_mask = mask | self.getMask(available)
                dp[new_mask] = min(dp[new_mask], dp[mask] + 1)
            else:
                for new_courses in combinations(available, k):
                    new_mask = mask | self.getMask(new_courses)
                    dp[new_mask] = min(dp[new_mask], dp[mask] + 1)
        return dp[(1 << n) - 1]
