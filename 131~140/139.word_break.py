from typing import *


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dict = set(wordDict)
        memo = {}
        return self.helper(s, memo, dict)

    def helper(self, s, memo, dict):
        if s in memo:
            return memo[s]
        if s in dict:
            return True
        for i in range(1, len(s)):
            if s[:i] in dict and self.helper(s[i:], memo, dict):
                memo[s] = True
                return True
        memo[s] = False
        return False


if __name__ == '__main__':
    s = Solution().wordBreak
    print(s("leetcode", ["leet", "code"]))