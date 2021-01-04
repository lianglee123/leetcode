from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        return self.helper(0, 0, len(inorder)-1, preorder, inorder)

    def helper(self, preStart, inStart, inEnd, preorder, inorder):
        if preStart > len(preorder) - 1  or inStart > inEnd:
            return None
        root = TreeNode(val=preorder[preStart])
        inIndex = 0 # index or current root in order
        for i in range(inStart, inEnd+1):
            if inorder[i] == root.val:
                inIndex = i
                break
        root.left = self.helper(preStart+1, inStart, inIndex-1, preorder, inorder)
        root.right = self.helper(preStart+(inIndex-inStart+1), inIndex+1, inEnd, preorder, inorder)
        return root


class Solution2:
    def buildTree(self, preorder, inorder):
        if inorder:
            ind = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[ind])
            root.left = self.buildTree(preorder, inorder[0:ind])
            root.right = self.buildTree(preorder, inorder[ind+1:])
            return root