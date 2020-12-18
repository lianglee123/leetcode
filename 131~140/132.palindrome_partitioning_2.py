class Solution:
    def minCut(self, s: str) -> int:
        size = len(s)
        if size <= 1:
            return 0

        dp = [i for i in range(size)]
        for i in range(1, size):
            if self.isPalindrome(s, 0, i):
                dp[i] = 0
            else:
                for j in range(i):
                    if self.isPalindrome(s, j+1, i):
                        dp[i] = min(dp[i], dp[j]+1)
        return dp[-1]

    def isPalindrome(self, s, left, right):
        """该函数依然可以用DP优化，参考第五题"""
        any()
        pass


