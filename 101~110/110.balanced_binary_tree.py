from typing import *
from functools import lru_cache


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        leftDep = self.maxDepth(root.left)
        rightDep = self.maxDepth(root.right)
        return abs(leftDep-rightDep) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)

    def maxDepth(self, node):
        """"maxDepth 重复执行，有优化空间，应该从下往上"""
        if not node:
            return 0
        return 1 + max(self.maxDepth(node.left), self.maxDepth(node.right))


class Solution2:
    def isBalanced(self, root):
        return self.dfsHeight(root) != -1

    def dfsHeight(self, root):
        if not root:
            return 0
        leftHeight = self.dfsHeight(root.left)
        if leftHeight == -1:
            return -1

        rightHeight = self.dfsHeight(root.right)
        if rightHeight == -1:
            return -1

        if abs(leftHeight - rightHeight) > 1:
            return -1

        return max(leftHeight, rightHeight) + 1
