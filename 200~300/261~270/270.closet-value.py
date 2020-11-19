from typing import *


class TreeNode:
    def __init__(self, val, left, right):
        self.val = 0
        self.left = left
        self.right = right


class Solution:
    """
    log(n)的复杂度
    这个理解起来其实非常精巧
    https://blog.csdn.net/haoxiaoxiaoyu/article/details/79809794
    """
    def closestValue(self, root: TreeNode, target):
        res = root.val
        while root:
            if abs(target-root.val) < abs(target-res):
                res = root.val
            root = root.left if root.val > target else root.right
        return res

class Solution2:
    """
    """
    def closestValue(self, root: TreeNode, target):
        res = root.val

    def helper(self, root, target, val):
        if not root: return val
        if abs(root.val - target) < abs(val - target):
            val = root.val
        if root.val < target:  #当root.val小于target时，一定要向右探索，因为左边的一定时更小的
            val = self.helper(root.right, target, val)
        elif root.val > target:
            val = self.helper(root.left, target, val)
        return val