from typing import *




class Solution:
    """
    dp[i][j]为以（i,j)为右下角的最大的正方形边长
    dp[i][j] = 1 + min(dp[i-1, j], dp[i-1, j-1], dp[i, j-1]) if m[i,j] = 1
    else: 0

    """
    def maximalSquare(self, m: List[List[str]]) -> int:
        if not m or not m[0]:
            return 0
        dp = [[0] * len(m[0]) for _ in range(len(m))]
        res = 0
        for i in range(1, len(m)):
            for j in range(len(m[0])):
                if i == 0 or j == 0:
                    dp[i][j] = 1 if m[i][j] == '1' else 0
                elif m[i][j] == '0':
                    dp[i][j] = 0
                else:
                    dp[i][j] = 1 + min(dp[i-1][j-1], dp[i][j-1], dp[j][i-1])
                res = max(dp[i][j])
        return res
