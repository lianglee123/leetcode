# https://leetcode.com/problems/recover-binary-search-tree/discuss/32539/Tree-Deserializer-and-Visualizer-for-Python
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return 'TreeNode({})'.format(self.val)

from collections import deque
def serialize(node):
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
            if not n:
                res.append(None)
                nextLevel.append(None)
                nextLevel.append(None)
            else:
                res.append(n.val)
                nextLevel.append(n.left or None)
                nextLevel.append(n.right or None)
        if any(i is not None for i in nextLevel):
            q.extendleft(nextLevel)
            print(q)
            levelCount = len(nextLevel)
    for i in range(len(res)-1, -1, -1):
        if res[i] == None:
            continue
        else:
            break
    return "[" + ','.join('None' if v is None else str(v) for v in res[:i+1]) + "]"


def deserialize(string):
    if string == '{}':
        return None
    nodes = [None if val in ('None', 'null') else TreeNode(int(val))
             for val in string.strip('[]{}').split(',')]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left  = kids.pop()
            if kids: node.right = kids.pop()
    return root


import turtle


def drawtree(root):
    def height(root):
        return 1 + max(height(root.left), height(root.right)) if root else -1
    def jumpto(x, y):
        t.penup()
        t.goto(x, y)
        t.pendown()
    def draw(node, x, y, dx):
        if node:
            t.goto(x, y)
            jumpto(x, y-20)
            t.write(node.val, align='center', font=('Arial', 12, 'normal'))
            draw(node.left, x-dx, y-60, dx/2)
            jumpto(x, y-20)
            draw(node.right, x+dx, y-60, dx/2)
    t = turtle.Turtle()
    t.speed(0)
    turtle.delay(0)
    h = height(root)
    jumpto(0, 30*h)
    draw(root, 0, 30*h, 40*h)
    t.hideturtle()
    turtle.mainloop()


if __name__ == '__main__':
    # drawtree(deserialize('[1,2,3,null,null,4,null,null,5]'))
    n = deserialize('[1,2,3,4,5,null,null,6]')
    # drawtree(deserialize('[1,2,3,4,5,null,6,7,null,null,null,null,8]'))
    print(serialize(deserialize('[1,2,3,4,5,null,null,6]')))
