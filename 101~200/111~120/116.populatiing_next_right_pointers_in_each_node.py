class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root) -> Node:
        if not root:
            return root
        if root.left:
            root.left.next = root.right
        if root.right and root.next:
            root.right.next = root.next.left
        self.connect(root.left)
        self.connect(root.right)


class Solution2:
    def connect(self, root) -> Node:
        if not root or not root.left:
            return root
        self.connectNodes(root.left, root.right)

    def connectNodes(self, node1, node2):
        node1.next = node2
        if node1.left:
            self.connectNodes(node1.right, node2.left)
            self.connectNodes(node1.left, node1.right)
            self.connectNodes(node2.left, node2.right)
            