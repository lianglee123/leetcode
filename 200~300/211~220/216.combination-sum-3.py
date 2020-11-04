from typing import *



class Solution:
    """
    尤其注意该方法是如何去重和剪枝的
    两个去重点：
        1. 使用start~10, 保证一条路径上的不使用一个元素两次。
        2. 每个节点按照start->10的顺序迭代，使其path也不会重复(最终path的元素是按照从大到小的顺序排列的), 所以res不用使用set去重

    """
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        self.dfs(res, [], k, 1, n)
        return res


    def dfs(self, res: List[List[int]], path: List[int], k, start, target):
        if len(path) == k or target <= 0:  # 满足条件就结束
            if len(path) == k and target == 0:
                res.append(path[:])
            return
        for i in range(start, 10):
            path.append(i)
            self.dfs(res, path, k, start+1, target-i)
            path.pop()


if __name__ == '__main__':
    s = Solution


