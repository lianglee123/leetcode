from typing import *


class TreeNode:
    def __init__(self, val, left, right):
        self.val = 0
        self.left = left
        self.right = right


class Solution1:
    """
    方案1，使用中序遍历保存所有数组。然后使用二分法在数组中寻找
    这种方案步骤多，效率低。
    https://www.cnblogs.com/grandyang/p/5247398.html
    """
    def closestKValues(self, root, target, k):
        pass

from collections import deque


class Solution2:
    """
    中序遍历，是从大到小的按顺序遍历，所以遍历的元素与目标值的差值
    https://www.cnblogs.com/grandyang/p/5247398.html
    """
    def closestKValues(self, root, target, k):
        res = deque()
        self.inorder(root, target, res, k)
        return res

    def inorder(self, root: TreeNode, target: int, res: deque, k: int):
        if not root: return
        if root.left:
            self.inorder(root.left, target, res, k)
        if len(res) < k:
            res.append(root.val)
        else:
            if abs(root.val-target) < abs(res[0] - target):
                res.popleft(0)
                res.append(root.val)
            else:
                return
        if root.right:
            self.inorder(root.right, target, res, k)


import heapq


class Solution3:
    """
    使用堆，有个trick要注意：
    1. 要求最小的k个值使用的是最大堆，因为堆只能pop堆顶的元素，所以要把最大值pop出去
    2. 相比solution2, 这种做法容易理解。因为solution2你要理解为什么一个数组的pop,append会得出正确结果
    """
    def closestKValues(self, root, target, k):
        res = []
        self.inorder(root, target, k, res)
        return [r[1] for r in res]

    def inorder(self, root: TreeNode, target: int, k: int, res: List[Tuple]):
        if not root:
            return
        if root.left:
            self.inorder(root.left, target, k, res)
        if len(res) < k:
            heapq.heappush(res, (abs(target-root.val), root.val))
        else:
            if res[0][0] > abs(target-root.val):
                heapq.heappop(res, (abs(target-root.val), root.val))
            else:
                return
        if root.right:
            self.inorder(root.right, target, k, res)
