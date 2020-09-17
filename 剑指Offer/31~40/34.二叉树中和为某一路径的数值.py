from typing import *


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


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
