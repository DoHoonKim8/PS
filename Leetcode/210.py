from collections import defaultdict, deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = [0] * numCourses
        for prerequisite in prerequisites:
            a, b = prerequisite[0], prerequisite[1]
            graph[b].append(a)
            indegree[a] += 1

        queue = deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)
        answer = []
        while queue:
            curr = queue.popleft()
            answer.append(curr)
            for succ in graph[curr]:
                indegree[succ] -= 1
                if indegree[succ] == 0:
                    queue.append(succ)
        if len(answer) < numCourses:
            return []
        else:
            return answer
