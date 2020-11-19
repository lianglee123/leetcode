from typing import *


class Solution:
    def numWays(self, n):
        if not n:
            return 1
        if n <= 2:
            return n
        pre = 1
        cur = 2
        for i in range(3, n+1):
            cur, pre = cur+pre, cur
        return cur

if __name__ == '__main__':
    s = Solution().numWays
    print(s(2))
    print(s(7))
    print(s(0))


