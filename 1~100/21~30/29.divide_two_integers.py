class Solution:
    MAX = (1 << 31) - 1
    MIN = -(1 << 31)
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == Solution.MIN and divisor == -1:
            return Solution.MAX
        sign_flag = (dividend > 0) == (divisor > 0)  # 与或
        sign = 1 if sign_flag else -1

        a = abs(dividend)
        b = abs(divisor)
        res = 0
        while a >= b:
            p = 1
            t = b
            while (t << 1) <= a:
                t = t << 1
                p = p << 1
            a -= t
            res += p
        return sign * res


if __name__ == '__main__':
    s = Solution().divide
    print(s(10, 3))
    # print(s(3, 3))
    print(s(7, -3))
