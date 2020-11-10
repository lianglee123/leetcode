from typing import *

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val  = val
        self.left = left
        self.right = right

class Integer:
    def __init__(self, val):
        self.val = val


class Solution:
    """
    https://www.cnblogs.com/lightwindy/p/9795764.html
    """
    def countUnivalSubtrees(self, root):
        c = Integer(0)
        self.isUnivalSubtrees(root, c)
        return c.val

    def isUnivalSubtrees(self, root, count):
        if not root:
            return True
        left = self.isUnivalSubtrees(root.left, count)
        right = self.isUnivalSubtrees(root.right, count)
        if left and right:
            if root.left and root.left.val != root.val:
                return False
            if root.right and root.right.val != root.val:
                return False
            count.val += 1
            return True
        return False




