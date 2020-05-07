class Solution:
    MAX = 2**31
    MIN = -2**31
    def reverse(self, x: int) -> int:
        res = 0
        sign = 1 if x > 0 else -1
        x = abs(x)
        while x:
            res = (res * 10) + x % 10
            x = x // 10
        res = sign * res
        if res < Solution.MIN or res > Solution.MAX:
            return 0
        else :
            return res