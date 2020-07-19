from utils.tree_node_utils import drawtree, deserialize


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        self._flatten(root)

    def _flatten(self, node):
        if not node:
            raise ValueError("node is empty")
        if node.left and node.right:
            left_head, left_tail = self._flatten(node.left)
            right_head, right_tail = self._flatten(node.right)
            left_tail.right = right_head
            node.left = None
            node.right = left_head
            return node, right_tail
        elif node.left:
            left_head, left_tail = self._flatten(node.left)
            node.left = None
            node.right = left_head
            return node, left_tail
        elif node.right:
            right_head, right_tail = self._flatten(node.right)
            node.left = None
            node.right = right_head
            return node, right_tail
        else:
            node.left = None
            return node, node


if __name__ == '__main__':
    root = deserialize("[1,2,5,3,4,null,6]")
    # drawtree(root)
    Solution().flatten(root)
    drawtree(root)
