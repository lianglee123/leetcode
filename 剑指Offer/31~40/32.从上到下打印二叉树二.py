from typing import *

from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        q = deque()
        res = []
        q.appendleft(root)
        while q:
            levelCount = len(q)
            levelValues = []
            while levelCount:
                n = q.pop()
                levelValues.append(n.val)
                if n.left:
                    q.appendleft(n.left)
                if n.right:
                    q.appendleft(n.right)
                levelCount -= 1
            res.append(levelValues)
        return res


if __name__ == '__main__':
    from utils import drawtree, deserialize, serialize
    n = deserialize("[3,9,20,null,null,15,7]")
    print(n, type(n))
    s = Solution().levelOrder
    print(s(n))