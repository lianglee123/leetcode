from typing import *
from functools import lru_cache

class Solution:
    @lru_cache(maxsize=1000)
    def cuttingRope(self, n: int) -> int:
        # print(n)
        if n == 2:
            return 1
        if n == 3:
            return 2

        res = 0
        for i in range(2, n//2+1):
            print(i, n-i)
            res = max(res, max(self.cuttingRope(i), i) * max(self.cuttingRope(n-i), n-i)) % 1000000007
        return res



if __name__ == '__main__':
    s = Solution().cuttingRope
    print(s(10))
    print(s(3))
    print(s(4))
