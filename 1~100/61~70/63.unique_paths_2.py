from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        g = obstacleGrid

        row, col = len(g), len(g[0])
        if g[row-1][col-1] == 1:
            return 0

        dp = [[0] * col for i in range(row)]
        dp[0][0] = 1

        for i in range(row):
            for j in range(col):
                if g[i][j] == 1:
                    dp[i][j] = 0
                else:
                    left = dp[j-1] if j-1 >= 0 else 0
                    top = dp[j-1] if i-1 >= 0 else 0
                    dp[i][j] = left + top
        return dp[row-1][col-1]
    