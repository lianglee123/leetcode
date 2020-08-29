class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """
    https://www.cnblogs.com/grandyang/p/5172838.html
    """
    def upsideDownBinaryTree(self, root):
        if not root or not root.left:
            return root
        l = root.left
        r = root.right
        res = self.upsideDownBinaryTree(l)
        l.left = r
        l.right = root
        root.left = None
        root.right = None
        return res


class Solution2:
    def upsideDownBinaryTree(self, root):
        cur = root
        pre = None
        temp = None
        while cur:
            next = cur.left
            cur.left = temp
            temp = cur.right
            cur.right = pre
            pre = cur
            cur = next
        return pre