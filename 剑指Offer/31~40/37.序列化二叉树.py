from typing import *


from collections import deque


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, node):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not node:
            return '[]'
        q = deque()
        q.appendleft(node)
        levelCount = 1
        res = []
        while q:
            nextLevel = []
            while levelCount:
                levelCount -= 1
                n = q.pop()
                res.append(n.val if n else None)
                if n is not None:
                    nextLevel.append(n.left or None)
                    nextLevel.append(n.right or None)
            if any(i is not None for i in nextLevel):
                q.extendleft(nextLevel)
                levelCount = len(nextLevel)
        for i in range(len(res)-1, -1, -1):
            if res[i] == None:
                continue
            else:
                break
        return "[" + ','.join('None' if v is None else str(v) for v in res[:i+1]) + "]"


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == '[]':
            return None
        nodes = [None if val in ('None', 'null') else TreeNode(int(val))
                 for val in data.strip('[]{}').split(',')]
        kids = nodes[::-1]
        root = kids.pop()
        for node in nodes:
            if node:
                if kids: node.left  = kids.pop()
                if kids: node.right = kids.pop()
        return root


if __name__ == '__main__':
    from utils import deserialize, serialize, drawtree
    n = Codec().deserialize("[5,2,3,null,null,2,4,3,1]")
    drawtree(n)
    print(Codec().serialize(n))
