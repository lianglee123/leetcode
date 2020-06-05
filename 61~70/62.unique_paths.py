
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        dp[m, n] = dp[
        :param m:
        :param n:
        :return:
        """
        dp = [[0]*m for i in range(n)]
        dp[0] = [1] * m
        for row in dp:
            row[0] = 1
        for row in range(1, n):
            for col in range(1, m):
                top = dp[row-1][col]
                left = dp[row][col-1]
                dp[row][col] = left + top
        return dp[n-1][m-1]


