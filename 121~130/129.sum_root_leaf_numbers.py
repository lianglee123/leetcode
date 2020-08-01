
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        self.sum = 0
        self.h(0, root)
        return self.sum

    def h(self, preLevelVal, node):
        if not node:
            return
        levelVal = preLevelVal * 10 + node.val
        if self.isLeaf(node):
            self.sum += levelVal
            return
        if node.left:
            self.h(levelVal, node.left)
        if node.right:
            self.h(levelVal, node.right)

    def isLeaf(self, node):
        return node and (not node.left) and (not node.right)


if __name__ == '__main__':
    from utils import *
    s = Solution().sumNumbers
    node = deserialize("[1,2,3]")
    # drawtree(node)
    assert_eq(s(deserialize("[1,2,3]")), 25)