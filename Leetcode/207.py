from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = [0] * numCourses
        for prerequisite in prerequisites:
            succ, pred = prerequisite[0], prerequisite[1]
            graph[pred].append(succ)
            indegree[succ] += 1
        queue = deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)
        num_taken = 0
        while len(queue) > 0:
            curr = queue.popleft()
            num_taken += 1
            for succ in graph[curr]:
                indegree[succ] -= 1
                if indegree[succ] == 0:
                    queue.append(succ)
        return num_taken == numCourses
