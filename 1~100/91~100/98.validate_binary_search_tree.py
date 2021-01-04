from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None




class Solution:
    """
    中序遍历的结果，就是按照顺序排列的结果
    """
    def isValidBST(self, root: TreeNode):
        stack = []
        cur = root
        val = None
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            if val is not None and val >= cur.val:
                return False
            val = cur.val
            cur = cur.right
        return True


class Solution2(object):
    def isSameTree(self, p, q):
        stack = [(p, q)]
        while stack:
            n1, n2 = stack.pop()
            if not n1 and not n2: continue
            if not n1 or not n2: return n1 == n2
            if n1.val != n2.val: return False
            stack.append((n1.right, n2.right))
            stack.append((n1.left, n2.left))
        return True


import collections

class Solution3(object):
    def isSameTree(self, p, q):
        queue = collections.deque([(p, q)])
        while queue:
            n1, n2 = queue.popleft()
            if not n1 and not n2: continue
            if not n1 or not n2: return n1 == n2
            if n1.val != n2.val: return False
            queue.append((n1.left, n2.left))
            queue.append((n1.right, n2.right))
        return True
