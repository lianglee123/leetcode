from typing import *


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        r, l = root.right, root.left
        root.right = self.invertTree(l)
        root.left = self.invertTree(r)
        return root


if __name__ == '__main__':
    s = Solution().invertTree

