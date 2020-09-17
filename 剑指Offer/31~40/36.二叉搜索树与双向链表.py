from typing import *


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return root
        inOrderNodes = self.inOrder(root)
        for i in range(len(inOrderNodes)):
            if i == (len(inOrderNodes)-1):
                inOrderNodes[i].right = inOrderNodes[0]
            else:
                inOrderNodes[i].right = inOrderNodes[i+1]
            inOrderNodes[i].left = inOrderNodes[i-1]
        return inOrderNodes[0]

    def inOrder(self, root):
        if not root:
            return []
        stack = []
        res = []

        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            if stack:
                root = stack.pop()
                res.append(root)
                root = root.right
        return res

    def inOrder2(self, root, res):
        if root:
            self.inOrder2(root.left, res)
            if len(res) > 0:
                res[-1].right = root
                root.left = res[-1]
            res.append(root)
            self.inOrder2(root.right, res)


class Solution2:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return root
        res = []
        self.inOrder2(root, res)
        res[-1].right = res[0]
        res[0].left = res[-1]
        return res[0]

    def inOrder2(self, root, res):
        if root:
            self.inOrder2(root.left, res)
            if len(res) > 0:
                res[-1].right = root
                root.left = res[-1]
            res.append(root)
            self.inOrder2(root.right, res)

class Solution3:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return root
        guard = self.pre = Node(0)
        self.inOrder(root)
        self.pre.right = guard.right
        guard.right.left = self.pre
        return guard.right

    def inOrder(self, root):
        if root:
            self.inOrder(root.left)
            self.pre.right = root
            root.left = self.pre
            self.pre = root
            self.inOrder(root.right)
