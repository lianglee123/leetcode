from typing import *


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class WrongSolution:
    def isSymmetric(self, root: TreeNode) -> bool:
        values = []
        self.inOrder(values, root)
        i, j = 0, len(values) - 1
        while i < j:
            if values[i] == values[j]:
                i += 1
                j -= 1
            else:
                return False
        return True

    def inOrder(self, res, root: TreeNode):
        if root:
            self.inOrder(res, root.left)
            res.append(root.val)
            self.inOrder(res, root.right)
        return


class Solution:
    """
    L.val = R.val
    L.L Symmetric  R.R
    L.R Symmetric R.L

    """
    def isSymmetric(self, root: TreeNode) -> bool:
        def recur(L, R):
            if not L and not R: return True
            if not L or not R or L.val != R.val: return False
            return recur(L.left, R.right) and recur(L.right, R.left)
        return recur(root.left, root.right) if root else True


if __name__ == '__main__':
    from utils import *
    n = deserialize("[1,2,2,2,null,2]")
    s = Solution().isSymmetric
    print(s(n))
