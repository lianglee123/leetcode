from typing import List


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


class Solution:
    """回溯，DFS"""
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        result = []
        self.dfs(result, root, [], sum)
        return result

    def dfs(self, result, node, path: List, sum):
        if not node:
            return
        path.append(node.val)
        sum -= node.val
        if self.isLeaf(node) and sum == 0:
            result.append(path[:])
        else:
            self.dfs(result, node.left, path, sum)
            self.dfs(result, node.right, path, sum)
        path.pop()


    def isLeaf(self, node):
        return node and (node.left is None) and (node.right is None)


if __name__ == '__main__':
    root = deserialize("[5,4,8,11,null,13,4,7,2,null,null,5,1]")
    sum = 22
    result = Solution().pathSum(root, sum)
    print(result)