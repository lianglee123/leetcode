class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List
from collections import deque



class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
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
        res.reverse()
        return res


class Solution2:
    """
    DFS: https://leetcode.com/problems/binary-tree-level-order-traversal-ii/discuss/34981/My-DFS-and-BFS-java-solution
    """
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        pass
    