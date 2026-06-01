from typing import List, Dict, DefaultDict
from collections import defaultdict

class Solution:
    def dfs(self, graph: DefaultDict[int, list], path: List[int], node: int, colors: str, dp: Dict[int, DefaultDict[str, int]]) -> Dict[str, int] | int:
        if dp.get(node) is not None:
            return dp[node]
        path[node] = 1
        color_values = defaultdict(int)
        for adj in graph[node]:
            if path[adj] == 1:
                return -1
            res = self.dfs(graph, path, adj, colors, dp)
            if res == -1:
                return -1
            else:
                for (color, value) in res.items():
                    color_values[color] = max(color_values[color], value)
        color_values[colors[node]] += 1
        dp[node] = color_values
        path[node] = 0
        return color_values

    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for edge in edges:
            a, b = edge[0], edge[1]
            graph[a].append(b)
        max_color_value = 0
        dp = dict()
        for i in range(len(colors)):
            path = [0] * len(colors)
            res = self.dfs(graph, path, i, colors, dp)
            if res == -1:
                return -1
            color_value = max(res.values())
            max_color_value = max(max_color_value, color_value)
        return max_color_value
