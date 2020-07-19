class Solution:
    def minDepth(self, root):
        if not root:
            return 0
        if not root.left:  # 注意这里，一个完全偏置的树，其minDepth不是为0
            return 1 + self.minDepth(root.right)
        if not root.right:
            return 1 + self.minDepth(root.left)
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1

