from typing import *


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        temp = root.left
        root.left = self.mirrorTree(root.right)
        root.right = self.mirrorTree(temp)
        return root


class Solution2:
    """
    隐式栈转化为显式栈的精髓就在这里
    """
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if not root: return root
        stack = [root]
        while stack:
            node = stack.pop()
            if node.left: stack.append(node.left)
            if node.right: stack.append(node.right)
            node.left, node.right = node.right, node.left
        return root



if __name__ == '__main__':
    from utils import deserialize, serialize
    s = Solution().mirrorTree
    n = deserialize("[4,2,7,1,3,6,9]")
    print(serialize(s(n)))
