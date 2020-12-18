from typing import *



class Solution:
    def cuttingRope(self, n):
        dp = [0] * 1001
        dp[1] = 1
        dp[2] = 1
        dp[3] = 2
        dp[4] = 4
        dp[5] = 6
        dp[6] = 9
        for i in range(7, n):
            dp[i] = (dp[i-3] * 3) % 1000000007
        return dp[n]
