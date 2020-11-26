from typing import *


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = 0
        self.left = left
        self.right = right


class Solution:
    """
    O(n)
    https://www.cnblogs.com/grandyang/p/5252599.html
    """
    def longestConsecutive(self, root: TreeNode):
        return self.dfs(root, None, 0)

    def dfs(self, child, parent, l):
        if not child: return 0
        l = l + 1 if parent and parent.val == child.val-1 else 1
        return max(l, self.dfs(child.left, child, l),self.dfs(child.right, child, l))


class Solution2:
    def longestConsecutive(self, root: TreeNode):
        return self.dfs(root, root.val, 0)
    def dfs(self, root, parentVal, count):
        if not root: return count

        if root.val == parentVal + 1:
            count = count + 1
        else:
            count = 1
        return max(count, self.dfs(root.left, root.val, count),
                   self.dfs(root.right, root.val, count))


