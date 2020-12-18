from typing import *


class Solution:
    """
    DP
    DP[i,i] = true
    DP[i,i+1] = Si == Si+1
    DP[i+1,j+1] = Si+1 == Sj+1 if dp[i,j] else false
    """
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        ans = ""
        dp = [[None] * len(s) for i in range(0, len(s))]
        for distance in range(0, len(s)):
            for start in range(len(s)):
                end = start + distance
                if end >= len(s):
                    break
                if distance == 0:
                    dp[start][end] = True
                elif distance == 1:
                    dp[start][end] = s[start] == s[end]
                else:
                    dp[start][end] = s[start] == s[end] and dp[start+1][end-1]

                if dp[start][end] and distance + 1 > len(ans):
                    ans = s[start:end+1]
        return ans


class Solution2:
    """
    方法二是扩展法
    直觉上，我很难实现扩展位置的迭代，因为有一种开始位置是从两个字符中间开始的，
    这种应该怎么处理呢？
        1. 一种方法，在原字符中插入特殊的字符，但我觉得这种方法好Low
        2. 如下，非常普通，但对我来说，这种方法太惊艳了。
    """
    def longestPalindrome(self, s: str) -> str:
        start, end = 0, 0
        for i in range(len(s)):
            left1, right1 = self.expandAroundCenter(s, i, i)
            left2, right2 = self.expandAroundCenter(s, i, i+1)
            if right1 - left1 > end - start:
                start, end = left1, right1
            if right2 - left2 > end - start:
                start, end = left2, right2
        return s[start:end+1]

    def expandAroundCenter(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1

