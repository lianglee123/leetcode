class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root:
            return 1 + max(self.maxDepth(root.right), self.maxDepth(root.left))
        else:
            return 0


if __name__ == '__main__':
    from utils.tree_node_utils import deserialize
    root = deserialize("[3,9,20,null,null,15,7]")
    s = Solution().maxDepth
    print(s(root))
    root = deserialize("[1, 2]")
    print(s(root))