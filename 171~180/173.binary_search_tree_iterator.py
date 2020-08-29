class BSTIterator:

    def __init__(self, root):
        self.stack = []
        self.__leftmost_inorder(root)

    def __leftmost_inorder(self, root):
        while root:
            self.stack.append(root)
            root = root.left

    def next(self):
        if not self.stack:
            raise StopIteration()
        topmost_node = self.stack.pop()
        if topmost_node.right:
            self.__leftmost_inorder(topmost_node.right)
        return topmost_node

    def hasNext(self):
        return len(self.stack) > 0

