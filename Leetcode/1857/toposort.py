from typing import List
from collections import defaultdict, deque

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        num_nodes = len(colors)
        indegree = [0] * num_nodes
        for edge in edges:
            a, b = edge[0], edge[1]
            graph[a].append(b)
            indegree[b] += 1
        color_values = [[0] * 26 for _ in range(num_nodes)]
        queue = deque()
        for i in range(num_nodes):
            if indegree[i] == 0:
                queue.append(i)
        while queue:
            curr = queue.popleft()
            color_values[curr][ord(colors[curr]) - ord('a')] += 1
            for succ in graph[curr]:
                for j in range(26):
                    color_values[succ][j] = max(color_values[succ][j], color_values[curr][j])
                indegree[succ] -= 1
                if indegree[succ] == 0:
                    queue.append(succ)
        # cycle
        if sum(indegree) != 0:
            return -1
        max_color_value = 0
        for i in range(len(color_values)):
            for j in range(26):
                max_color_value = max(max_color_value, color_values[i][j])
        return max_color_value
