from typing import List

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        q = deque()
        q.append(root)
        level = 0
        while q:
            row = []
            for i in range(len(q)):
                n = q.popleft()
                if n:
                    row.append(n.val)
                    if n.left:
                        q.append(n.left)
                    if n.right:
                        q.append(n.right)
            if level % 2 != 0:
                row.reverse()
            res.append(row)
            level += 1
        return res


if __name__ == '__main__':
    from utils.tree_node_utils import deserialize
    root = deserialize("[0,2,4,1,null,3,-1,5,1,null,6,null,8]")
    s = Solution().zigzagLevelOrder
    print(s(root))