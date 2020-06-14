from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    step1: find the swap ele
    step2:
    """
    firstNode = None
    secondNode = None
    preNode = TreeNode(val=float('-inf'))

    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.traverse(root)

        self.firstNode.val, self.secondNode.val = self.secondNode.val, self.firstNode.val


    def traverse(self, root):
        if not root:
            return None

        self.traverse(root.left)

        if self.firstNode is None and self.preNode.val >= root.val:
            self.firstNode = self.preNode

        if self.firstNode is not None and self.preNode.val >= root.val:
            self.secondNode = root

        self.preNode = root

        self.traverse(root.right)