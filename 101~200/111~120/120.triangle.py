from typing import *
from functools import lru_cache


class Solution:

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        self.triangle = triangle
        self.cache = [
            [None] * len(t)
        for t in triangle ]
        return self.getPathSum(0, 0)

    def getPathSum(self, level, index):
        if level >= len(self.triangle):
            return 0
        if self.cache[level][index] is not None:
            return self.cache[level][index]
        v = self.triangle[level][index]
        res = v + min(self.getPathSum(level+1, index), self.getPathSum(level+1, index+1))
        self.cache[level][index] = res
        return res



if __name__ == '__main__':
    a = [
        [2],
        [3,4],
        [6,5,7],
        [4,1,8,3]
    ]
    s = Solution().minimumTotal(a)
    print(s)