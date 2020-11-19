from typing import *



class Solution:
    """
    https://www.cnblogs.com/grandyang/p/4743837.html
    https://blog.csdn.net/qq508618087/article/details/50283715
    """
    def nthUglyNumber(self, n):
        res = [1]
        i2, i3, i5 = 0, 0, 0
        while len(res) < n:
            m2 = res[i2] * 2
            m3 = res[i3] * 3
            m5 = res[i5] * 5
            mn = min(m2, m3, m5)
            if mn == m2:
                i2 += 1
            elif mn == m3:
                i3 += 1
            else:
                i5 += 2
        return res.pop()

