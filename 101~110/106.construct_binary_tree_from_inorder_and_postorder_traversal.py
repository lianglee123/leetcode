from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if inorder:
            rIndex = inorder.index(postorder.pop())
            root = TreeNode(inorder[rIndex])
            root.right = self.buildTree(inorder[rIndex+1:], postorder)
            root.left = self.buildTree(inorder[:rIndex], postorder)
            return root


if __name__ == '__main__':
    from utils.tree_node_utils import deserialize
    root = deserialize("[0,2,4,1,null,3,-1,5,1,null,6,null,8]")
    s = Solution().buildTree
    print(s([9,3,15,20,7], [9,15,7,20,3]))