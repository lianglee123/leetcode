from typing import *
from functools import lru_cache

class Solution:
    @lru_cache(maxsize=1000)
    def cuttingRope(self, n: int) -> int:
        # print(n)
        if n == 2:  # 我觉得这个更笨就是错误的DP解法，你怎么知道是到2，3了就停止拆，而不是到4，5，6时也停止拆。这种是
            # 先知道了答案然后去套方法。
            return 1
        if n == 3:
            return 2

        res = 0
        for i in range(2, n//2+1):
            print(i, n-i)
            res = max(res, max(self.cuttingRope(i), i) * max(self.cuttingRope(n-i), n-i)) % 1000000007
        return res


class Solution2:

    def cuttingRope(self, n: int) -> int:
        dp = [0]*(n+1)
        for i in range(2, n+1):
            for j  in range(1, i):
                dp[i] = max(dp[i], j*(i-j), j*dp[i-j])
        return dp[n]



if __name__ == '__main__':
    s = Solution2().cuttingRope
    print(s(10))
    print(s(3))
    print(s(4))
    print(s(2))
