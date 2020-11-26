from typing import *


class Solution:
    """
    https://www.cnblogs.com/lightwindy/p/9552041.html
    """
    def minTotalDistance(self, grid):
        if not grid or not grid[0]:
            return 0
        ipos = []
        jpos = []
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j] == 1:
                    ipos.append(i)
                    jpos.append(j)
        jpos.sort()  # j需要排序，i不需要，因为i就是按顺序来的
        return self.countOneDimension(ipos) + self.countOneDimension(jpos)


    def countOneDimension(self, pos):
        res = 0
        i, j = 0, len(pos) - 1
        while i <= j:
            res += (pos[j] - pos[i])
            i += 1
            j -= 1
        return res



