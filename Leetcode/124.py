from typing import Tuple, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def max_path_sum_with_root(self, root_v, root_l, root_r) -> int:
        if root_l > 0 and root_r > 0:
            return root_l + root_r - root_v
        else:
            return max(root_l, root_r)

    def max_path_sum_aux(self, root: Optional[TreeNode]) -> Tuple[int, int, int]:
        # root를 포함하지 않으면: 왼쪽, 오른쪽 subtree의 optimal path 중에서 선택
        # root를 포함하면
        # 1) root를 시작으로 왼쪽으로 내려가는 path
        # 2) root를 시작으로 오른쪽으로 내려가는 path
        # 3) root와 왼쪽, 오른쪽을 둘 다 거치는 path
        if root is None:
            return (-1000, -1000, -1000)
        if root.left is None and root.right is None:
            return (root.val, root.val, root.val)

        left_opt, left_l, left_r = self.max_path_sum_aux(root.left)
        right_opt, right_l, right_r = self.max_path_sum_aux(root.right)
        
        without_root = max(left_opt, right_opt)
        root_l, root_r = root.val, root.val
        if max(left_l, left_r) > 0:
            root_l += max(left_l, left_r)
        if max(right_l, right_r) > 0:
            root_r += max(right_l, right_r)
        with_root = self.max_path_sum_with_root(root.val, root_l, root_r)
        root_opt = max(without_root, with_root)
        return (root_opt, root_l, root_r)

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        return self.max_path_sum_aux(root)[0]
