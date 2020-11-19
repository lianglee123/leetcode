from typing import *


class Solution:
    """
    https://www.cnblogs.com/grandyang/p/4741028.html
    """
    def addDigit(self, num):
        while num >= 10:
            s = 0
            while num > 0:
                a, b = divmod(num, 10)
                s += b
                num = a
            num = s
        return num


if __name__ == '__main__':
    s = Solution().addDigit
    for i in range(100):
        print(i, s(i))
