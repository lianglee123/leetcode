from typing import *

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        if x == 1:
            return 1
        if n == 0:
            return 1
        if n < 0:
            return self.myPow(1/x, -n)
        a, b = divmod(n, 2)
        v = self.myPow(x, a)
        if b:
            return x * v * v
        else:
            v = self.myPow(x, n//2)
            return v * v


class Solution2:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        if x == 1:
            return 1
        if n == 0:
            return 1
        if n < 0:
            n = -n
            x = 1/x
        res = 1
        while n > 1:
            n, r = divmod(n, 2)
            if r:
                res *= x
            x = x*x
        return res * x


if __name__ == '__main__':
    from utils import assert_eq
    s = Solution2().myPow
    assert_eq(s(2.0, 1), 2**1)
    assert_eq(s(2.0, 2), 2**2)
    assert_eq(s(-2.0, 10), (-2)**10)
