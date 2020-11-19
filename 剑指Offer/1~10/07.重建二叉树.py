from typing import *

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        self.i = 0
        return self.helper(preorder, 0, len(preorder), inorder)

    # [l, r)
    def helper(self, preorder: List[int], l, r, inorder):
        if self.i < len(preorder):
            root = TreeNode(preorder[self.i])
            j = inorder.index(preorder[self.i], l, r)
            if l < j:
                self.i += 1
                root.left = self.helper(preorder, l, j, inorder)
            if j+1 < r:
                self.i += 1
                root.right = self.helper(preorder, j+1, r, inorder)
            return root
        return

class Solution2:
    """提前计算indexMap"""
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        self.i = 0
        self.indexMap = {}
        for i, n in enumerate(inorder):
            self.indexMap[n] = i
        return self.helper(preorder, 0, len(preorder), inorder)

    # [l, r)
    def helper(self, preorder: List[int], l, r, inorder):
        if self.i < len(preorder):
            root = TreeNode(preorder[self.i])
            j = self.indexMap[preorder[self.i]]  # 根节点在中序列表中的索引
            if l < j:
                self.i += 1
                root.left = self.helper(preorder, l, j, inorder)
            if j+1 < r:
                self.i += 1
                root.right = self.helper(preorder, j+1, r, inorder)
            return root
        return


if __name__ == '__main__':
    from utils import *
    s = Solution2().buildTree
    preorder = [3,9,20,15,7]
    inorder =  [9,3,15,20,7]
    drawtree(s(preorder, inorder))