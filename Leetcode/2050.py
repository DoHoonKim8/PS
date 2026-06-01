from typing import List
from collections import defaultdict, deque

class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = defaultdict(list)
        indegree = [0] * (n + 1)
        for relation in relations:
            pre, succ = relation[0], relation[1]
            graph[pre].append(succ)
            indegree[succ] += 1
        queue = deque()
        end_time = [0] * (n + 1)
        for i in range(1, len(indegree)):
            if indegree[i] == 0:
                queue.append(i)
                end_time[i] = time[i - 1]

        result = 0
        while queue:
            curr = queue.popleft()
            result = max(result, end_time[curr])
            for succ in graph[curr]:
                end_time[succ] = max(end_time[curr] + time[succ - 1], end_time[succ])
                indegree[succ] -= 1
                if indegree[succ] == 0:
                    queue.append(succ)

        return result
