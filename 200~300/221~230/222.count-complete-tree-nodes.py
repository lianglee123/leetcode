from typing import *


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if root:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)
        return 0


class Solution2:
    """
    https://leetcode-cn.com/problems/count-complete-tree-nodes/solution/chang-gui-jie-fa-he-ji-bai-100de-javajie-fa-by-xia/
    这个实在是妙
    如果left == right， 说明左节点一定是满的，所以可以直接求出答案。
    如果left != right(left > right), 说明右节点比左节点少了一层，但是右节点是满的。
    所以可以递归的求下去
    但是这种求法有个问题，就是可能反复的遍历一个节点去求高度
    """
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        left = self.countLevel(root.left)
        right = self.countLevel(root.right)
        if left == right:
            return 2**left + self.countNodes(root.right)
        else:
            return 2**right + self.countNodes(root.left)

    def countLevel(self, root):
        level = 0
        while root:
            level += 1
            root = root.left
        return level