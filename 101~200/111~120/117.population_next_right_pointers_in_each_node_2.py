
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    """
    注意和116相比的空位连接
    """
    def connect(self, root):
        if not root:
            return None
        if root.left:
            root.left.next = root.right if root.right else self.findNext(root.next)
        if root.right:
            root.right.next = self.findNext(root.next)
        self.connect(root.right)
        self.connect(root.left)
        return root

    def findNext(self, root):
        if not root: return None
        if root.left:
            return root.left
        if root.right:
            return root.right
        return self.findNext(root.next)



def deserialize(string):
    if string == '{}':
        return None
    nodes = [None if val == 'null' else Node(int(val))
             for val in string.strip('[]{}').split(',')]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left  = kids.pop()
            if kids: node.right = kids.pop()
    return root


if __name__ == '__main__':
    root = deserialize('[1,2,3,4,5,null,6,7,null,null,null,null,8]')

    Solution().connect(root)