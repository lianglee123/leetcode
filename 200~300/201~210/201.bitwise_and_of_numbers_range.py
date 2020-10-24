from typing import *


class Solution:
    """
    该题转化为数学问题，就是求M和N的二进制字符串最长公共前缀
    其证明如下：https://leetcode-cn.com/problems/bitwise-and-of-numbers-range/solution/si-lu-jian-dan-xing-neng-da-dao-100-by-jamleon-8/
    """
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        t = 0
        while m < n:
            m = m >> 1
            n = n >> 1
            t += 1
        return m << t

