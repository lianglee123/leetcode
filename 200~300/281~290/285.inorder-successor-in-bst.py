from typing import *


class TreeNode:
    def __init__(self, val, left, right):
        self.val = 0
        self.left = left
        self.right = right


class Solution:
    """
    我理解的这题就是要找第一个大于node的节点
    方法一，inorder遍历，寻找当前节点的下一个节点， 复杂度O(N)， 这种方法对非BST也适用
    https://www.cnblogs.com/grandyang/p/5306162.html
    """
    def inorderSucccesor(self, root: TreeNode, node: TreeNode):
        seenNode = False
        stk = []
        while stk or root:
            while root:
                stk.append(root)
                root = root.left
            root = stk.pop()
            if seenNode:
                return root
            if root == node:
                seenNode = True
            root = root.right
        return None

class Solution2:
    """
    这题就是要找第一个大于node的节点
    https://www.cnblogs.com/grandyang/p/5306162.html
    这个原理费城精妙，和那个找closet-values一样精妙
    思考：因为是中序，所以比p刚好大一的那个值，一定是在找P的路径上
    """
    def inorderSucccesor(self, root: TreeNode, p: TreeNode):
        res = None
        while root:
            if root.val > p.val:
                res = root
                root = root.left
            else:
                root = root.right
        return res


class Solution3:
    """
    Solution2的递归做法
    也非常精妙
    """
    def inorderSucccesor(self, root: TreeNode, p: TreeNode):
        if not root:
            return None
        if root.val <= p.val:
            return self.inorderSucccesor(root.right, p)
        else:
            res = root
            res2 = self.inorderSucccesor(root.left, p)
        return res2 or res

