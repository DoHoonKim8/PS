from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda interval: interval[1])
        result = 0
        end = intervals[0][0]
        for interval in intervals:
            s, e = interval[0], interval[1]
            if s < end:
                result += 1
                continue
            end = e
        return result
