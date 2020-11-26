from typing import *


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = 0
        self.left = left
        self.right = right


from collections import deque


class Solution:
    """
    https://www.cnblogs.com/cnoodle/p/12453308.html
    # 这个解法最终会有很多的null在字符串末尾
    """
    def serialize(self, root)->str:
        if not root:
            return ""
        res = []
        q = deque()
        q.appendleft(root)
        while q:
            cur = q.pop()
            if not cur:
                res.append('null')
                continue
            res.append(str(cur.val))
            q.appendleft(cur.left)
            q.appendleft(cur.right)
        return ','.join(res)

    def deserialize(self, str)-> TreeNode:
        if not str:
            return None
        values = str.split(",")
        q = deque()
        root = TreeNode(int(values[0]))
        q.appendleft(root)
        i = 1
        while i < len(values):
            cur = q.pop()
            if not values[i] == 'null':
                cur.left = TreeNode(int(values[i]))
                q.appendleft(cur.left)
            i += 1
            if not values[i] == "null":
                cur.right = TreeNode(values[i])
                q.appendleft(cur.right)
            i += 1
        return root


class Codec:

    """
    leetcode上的大神StefanPochmann的答案,他的方案和Solution1是补营养的，
    他采用的是深度优先
    https://leetcode.com/problems/serialize-and-deserialize-binary-tree/discuss/74259/Recursive-preorder-Python-and-C%2B%2B-O(n)
    注意：工具库里的deserialize也是这位大神的杰作。
    """
    def serialize(self, root):
        res = []
        self._s(root, res)
        return ','.join(res)

    def _s(self, root, res):
        if root:
            res.append(str(root.val))
            self._s(root.left, res)
            self._s(root.right, res)
        else:
            res.append("null")

    def deserialize(self, data: str):
        if not data:
            return None
        values = data.split(",")
        root = TreeNode(int(values[0]))


if __name__ == '__main__':
    from utils.tree_node_utils import serialize, deserialize

    node = deserialize("[1,2,3,null,null,4,5]")
    s = Solution().serialize
    print(s(node))

    s2 = Codec().serialize
    print(s2(node))

