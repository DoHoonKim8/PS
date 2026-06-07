from typing import Optional, Tuple

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rob_aux(self, root: Optional[TreeNode]) -> Tuple[int, int]:
        if root is None:
            return (0, 0)
        max_without_left, max_with_left = self.rob_aux(root.left)
        max_without_right, max_with_right = self.rob_aux(root.right)
        without_root = max([max_without_left, max_with_left]) + max([max_without_right, max_with_right])
        with_root = root.val + max_without_left + max_without_right
        return (without_root, with_root)

    def rob(self, root: Optional[TreeNode]) -> int:
        return max(self.rob_aux(root))
