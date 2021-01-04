from typing import List

from copy import deepcopy


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def deserialize(string):
    if string == '{}':
        return None
    nodes = [None if val == 'null' else TreeNode(int(val))
             for val in string.strip('[]{}').split(',')]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left  = kids.pop()
            if kids: node.right = kids.pop()
    return root


def serialize(node):
    if not node:
        return '[]'
    queue = [node]
    values = []
    while queue:
        n = queue.pop()
        if n:
            values.append(str(n.val))
            if n.left or n.right:
                queue.insert(0, n.left)
                queue.insert(0, n.right)
        else:
            values.append('null')

    while values:
        if values[-1] == 'null':
            values.pop()
        else:
            break

    return '[' + ','.join(values) + ']'


def test_serializer():
    n = deserialize("[1,null,3,2]")
    assert serialize(n) == "[1,null,3,2]"
    n = deserialize("[3,2,null,1]")
    assert serialize(n) == "[3,2,null,1]"
    n = deserialize("[3,1,null,null,2]")
    assert serialize(n) == "[3,1,null,null,2]"
    n = deserialize("[2,1,3]")
    assert serialize(n) == "[2,1,3]"
    n = deserialize("[1,null,2,null,3]")
    assert serialize(n) == "[1,null,2,null,3]"

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return []
        return self.dfs(1, n, {})

    def dfs(self, start, end, memo):
        if (start, end) in memo:
            return memo[(start, end)]
        if start > end:
            v = [None]
            memo[(start, end)] = v
            return v
        ans = []
        for i in range(start, end+1):
            left = (start, i-1, memo)
            right = (i+1, end, memo)
            for l_node in deepcopy(self.dfs(*left)):
                for r_node in deepcopy(self.dfs(*right)):
                    ans.append(TreeNode(val=i, left=l_node, right=r_node))
        memo[(start, end)] = ans
        return ans


class Solution2:
    """
    击败5.3%的用户。。。。
    只要去掉deepCopy, 就变为93%了，本来也不需要deepCopy
    如果觉得要用deepCopy，说明你并没有理解。生成的树之间也并没有共用节点。
    """
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return []
        memo = [[None for j in range(n+1)] for i in range(n+1)]
        return self.dfs(n, 1, n, memo)

    def dfs(self, n, start, end, memo):
        if start <= n and end <= n and memo[start][end] != None:
            return memo[start][end]
        if start > end:
            return [None]
        ans = []
        for i in range(start, end+1):
            left = (n, start, i-1, memo)
            right = (n, i+1, end, memo)
            for l_node in deepcopy(self.dfs(*left)):
                for r_node in deepcopy(self.dfs(*right)):
                    ans.append(TreeNode(val=i, left=l_node, right=r_node))
        memo[start][end] = ans
        return ans


def test_solution():
    s = Solution2().generateTrees
    res = s(4)
    for n in res:
        print(serialize(n))

if __name__ == '__main__':
    test_serializer()
    test_solution()
