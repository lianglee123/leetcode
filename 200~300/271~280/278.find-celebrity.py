from typing import *


class Solution:
    """
    https://www.cnblogs.com/grandyang/p/5310649.html
    """
    def findCelebrity(self, n):
        res = 0
        for i in range(n):
            if self.knows(i, res):
                res = i
        for i in range(n):
            if res != i and self.knows(res, i) and not self.knows(i, res):
                return -1
        return res

    def knows(self, i, j)->bool:
        return True