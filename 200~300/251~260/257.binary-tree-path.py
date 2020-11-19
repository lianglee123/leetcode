from typing import *


class TreeNode:
    def __init__(self, val, left, right):
        self.val = 0
        self.left = left
        self.right = right


class Solution:

    def binaryTreePaths(self, root):
        if not root:
            return []
        res = []
        self.helper(res, [], root)

    def helper(self, res, path, root):
        path.append(root.val)
        if not root.left and not root.left:
            res.append(path[:])
        if root.left:
            self.helper(res, path, root)
        if root.right:
            self.helper(res, path, root)
        path.pop()


class Solution2:
    """
    方法2比方法1更高明，因为直接返回了题目要的结果。
    """
    def binaryTreePaths(self, root):
        if not root:
            return []
        res = []
        self.helper(res, "", root)

    def helper(self, res, path, root):
        if not root.left and not root.left:
            res.append(path + str(root.val))
        if root.left:
            self.helper(res, path + "->" + str(root.val), root)
        if root.right:
            self.helper(res, path + "->" + str(root.val), root)





