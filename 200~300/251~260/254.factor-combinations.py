from typing import *


class Solution:
    """
    https://www.cnblogs.com/grandyang/p/5332722.html
    """
    def getFactors(self, n):
        res = []
        self.traceBack(n, 2, res, [])
        return res

    def traceBack(self, n, start, res, path):  # 在递归黑奴是种传入start参数，起到了排序排序的作用。
        if n == 1:
            if len(path) > 1:
                res.append(path[:])
            return

        for i in range(start, n+1):
            if n % i != 0:
                continue
            path.append(i)
            self.traceBack(n//i, i, res, path)
            path.pop()
        return


import math


class Solution2:
    """
    优化, 把迭代终止条件变为sqrt(N)
    """
    def getFactors(self, n):
        res = []
        self.traceBack(n, 2, res, [])
        return res

    def traceBack(self, n, start, res, path):  # 在递归黑奴是种传入start参数，起到了排序排序的作用。
        if n == 1:
            if len(path) > 1:
                res.append(path[:])
            return

        for i in range(start, int(math.sqrt(n))+1):
            if n % i != 0:
                continue
            path.append(i)
            self.traceBack(n//i, i, res, path)
            path.pop()
        return


if __name__ == '__main__':
    s = Solution().getFactors
    print(s(32))

