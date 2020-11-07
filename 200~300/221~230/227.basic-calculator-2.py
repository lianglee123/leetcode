from typing import *
import math

class Solution:
    """
    加减法 + 空格 +  乘除
    """
    def calculate(self, s):
        stack = []
        num = 0
        sign = '+'
        for i, c in enumerate(s):
            if c.isdigit():
                num = 10 * num + (ord(c) - ord('0'))
            if (not c.isdigit() and c != " ") or i == len(s)-1:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    pre = stack.pop()
                    stack.append(pre * num)
                elif sign == '/':
                    pre = stack.pop()
                    stack.append(int(pre/num))
                sign = c
                num = 0
        return sum(stack)


if __name__ == '__main__':
    s = Solution().calculate
    print(s("14-3/2"))
