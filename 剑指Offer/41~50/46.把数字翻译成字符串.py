from typing import *



class Solution:
    """
    https://leetcode-cn.com/problems/ba-shu-zi-fan-yi-cheng-zi-fu-chuan-lcof/solution/mian-shi-ti-46-ba-shu-zi-fan-yi-cheng-zi-fu-chua-6/
    """
    def translateNum(self, num: int) -> int:
        s = str(num)
        a = b = 1
        for i in range(2, len(s) + 1):
            a, b = (a + b if "10" <= s[i - 2:i] <= "25" else a), a
        return a


class Solution2:
    def translateNum(self, num: int) -> int:
        s = str(num)
        a = b = 1
        for i in range(len(s) - 2, -1, -1):
            a, b = (a + b if "10" <= s[i:i + 2] <= "25" else a), a
        return a


class Solution3:
    def translateNum(self, num: int) -> int:
        a = b = 1
        y = num % 10
        while num != 0:
            num //= 10
            x = num % 10
            a, b = (a + b if 10 <= 10 * x + y <= 25 else a), a
            y = x
        return a
