class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.__isSymmetric(root.left, root.right)

    def __isSymmetric(self, left, right):
        if not left or not right:
            return left == right
        return left.val == right.val and \
               self.__isSymmetric(left.left, right.right) and \
            self.__isSymmetric(left.right, right.left)

from collections import deque

class Solution2:
    """
    按层次遍历，对比每一层
    """
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        q1 = deque()
        q1.append(root)
        q2 = deque()
        q2.append(root)
        while q1 and q2:
            if len(q1) != len(q2):
                return False
            for i in range(len(q1)):
                n1 = q1.popleft()
                n2 = q2.popleft()
                if bool(n1) != bool(n2):
                    return False
                if not n1:
                    continue
                if n1.val != n2.val:
                    return False
                q1.append(n1.left)
                q1.append(n1.right)

                q2.append(n2.right)
                q2.append(n2.left)
        return not q1 and not q2

    def levelIter(self, root):
        if not root:
            return []
        res = []
        q = deque()
        q.append(root)
        while q:
            for i in range(len(q)):
                n = q.popleft()
                if not n:
                    res.append(None)
                else:
                    res.append(n.val)
                    q.append(n.left)
                    q.append(n.right)
        return res




if __name__ == '__main__':
    from utils.tree_node_utils import deserialize
    root = deserialize('[1,2,2,3,4,4,3]')
    print(Solution2().isSymmetric(root))