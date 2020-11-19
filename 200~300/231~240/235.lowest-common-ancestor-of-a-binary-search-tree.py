from typing import *


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



class Solution:
    """
    这个方法，不过只要是二叉树都可以求出结果
    """
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left:
            return right
        if not right:
            return left
        return root


class Solution2:
    """
    这个方法能只能是二叉搜索树才行
    """
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val > q:
            return self.lowestCommonAncestor(root, q, p)
        while True:
            if root.val >= p.val and root.val <= q.val:
                return root
            elif root.val < p.val:
                root = root.right
            else:
                root = root.left


if __name__ == '__main__':
    s = Solution2().lowestCommonAncestor
    from utils.tree_node_utils import deserialize, drawtree
    node = deserialize("[6,2,8,0,4,7,9,null,null,3,5]")
    drawtree(node)
