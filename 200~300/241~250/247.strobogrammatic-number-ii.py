from typing import *


class Solution:
    """
    https://www.cnblogs.com/lightwindy/p/8491311.html
    """
    def findStrobogrammatic(self, n):
        return self.help(n, n)

    def help(self, n, m):
        if n == 0:return [""]  # n为偶数
        if n == 1: return ["0", "1", "8"] # n为奇书
        temp = self.help(n-2, m)
        res = []
        for i, s in enumerate(temp):
            if n != m:   # 最后一个不能加零
                res.append("0" + s + "0")
            res.append("1" + s + "1")
            res.append("8" + s + "8")
            res.append("6" + s + "9")
            res.append("9" + s + "6")
        return res


if __name__ == '__main__':
    s = Solution().findStrobogrammatic
    print(s(2))
