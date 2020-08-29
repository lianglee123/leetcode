from typing import *

class Solution:
    def numWays(self, n: int) -> int:
        if n <= 1:
            return 1
        pre = 0
        cur = 1
        for i in range(2, n+2):
            cur, pre = cur + pre, cur
        return cur

if __name__ == '__main__':
    s = Solution().numWays
    print(s(2))
    print(s(7))
    print(s(0))


