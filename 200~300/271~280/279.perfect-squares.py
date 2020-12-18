from typing import *


class Solution:
    """
    https://www.cnblogs.com/grandyang/p/4800552.html
    这个所谓的dp是一种自底向上的dp， 第一次碰到这种。
    """
    def numSquares(self, n: int) -> int:
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        for i in range(0, n+1):
            j = 1
            while i + j*j <=n:
                dp[i+j*j] = min(dp[i+j*j], dp[i]+1)
                j += 1
        return int(dp[-1])


class Solution2:
    def numSquares(self, n: int) -> int:
        dp = []
        while len(dp) < n:
            m = len(dp)
            val = float('inf')
            i = 1
            while i*i <= m:
                val = min(val, dp[m-i*i] + 1)
            dp.append(val)
        return dp[-1]


if __name__ == '__main__':
    s = Solution().numSquares
    print(s(12))
