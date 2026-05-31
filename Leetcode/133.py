class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        cloned = Node(node.val, None)
        stack = [(node, cloned)]
        copied = dict()
        copied[node.val] = cloned
        while stack:
            orig, copy = stack.pop()
            for adj in orig.neighbors:
                if adj.val in copied:
                    copy.neighbors.append(copied[adj.val])
                else:
                    cloned_node = Node(adj.val, None)
                    copied[adj.val] = cloned_node
                    stack.append((adj, cloned_node))
                    copy.neighbors.append(cloned_node)
        return cloned
