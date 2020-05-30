class SolutionBrute:
    """
    Time Limit EXcellet
    """
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n < 0:
            n = - n
            x = 1/x
        res = 1
        for i in range(n):
            res *= x
        return res


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n < 0:
            n = - n
            x = 1/x
        return self.myPow(x*x, n//2) if n % 2 == 0 else x * self.myPow(x*x, n//2)

class SolutionIter:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n < 0:
            n = - n
            x = 1/x
        res = 1
        while n > 0:
            if n == 1:
                return 0
            elif n == 0:
                return x
            else:
                x = x * x
                n = n >> 1
