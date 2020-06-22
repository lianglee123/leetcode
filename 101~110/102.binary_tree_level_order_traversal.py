class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import *
from collections import deque


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        q = deque()
        q.append(root)
        while q:
            level = []
            for i in range(len(q)):
                n = q.popleft()
                if n:
                    level.append(n.val)
                    if n.left:
                        q.append(n.left)
                    if n.right:
                        q.append(n.right)
            res.append(level)
        return res



if __name__ == '__main__':
    from utils.tree_node_utils import deserialize
    root = deserialize("[3,9,20,null,null,15,7]")
    s = Solution().levelOrder
    print(s(root))