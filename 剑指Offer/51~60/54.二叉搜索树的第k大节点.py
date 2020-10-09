from typing import *


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution1:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        self.res = []
        self.inOrderReverseIter(root)
        return self.res[k-1]

    def inOrderReverseIter(self, node):
        if not node:
            return
        self.inOrderReverseIter(node.left)
        self.res.append(node.val)
        self.inOrderReverseIter(node.right)


class Solution2:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        self.cnt = 0
        self.k = k
        found, val = self.inOrderReverseIter(root)
        if found:
            return val
        else:
            raise ValueError("not found")

    def inOrderReverseIter(self, node):
        if not node:
            return False, None
        found, val = self.inOrderReverseIter(node.right)
        if found:
            return True, val
        self.cnt += 1
        if self.cnt == self.k:
            return True, node.val
        return self.inOrderReverseIter(node.left)


if __name__ == '__main__':
    from utils import serialize, deserialize
    s = Solution2().kthLargest
    assert s(deserialize("[3,1,4,null,2]"), 1) == 4
    assert s(deserialize("[5,3,6,2,4,null,null,1]"), 3) == 4
