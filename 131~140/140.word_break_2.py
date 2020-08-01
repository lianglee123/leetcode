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


class Solution2:
    """
    这个和回溯没有一点关系，单纯的DP, 不过WordBreak1是回溯，因为它可以尽快的得到一个结果。
    """
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        if not s:
            return []
        dict = set(wordDict)
        self.memo = {}
        return self.convertRes(self.helper(s, dict))


    def helper(self, s, dict):
        res = []
        if not s:
            return res

        if s in self.memo:
            return self.memo[s]

        if s in dict:
            res.append([s])

        for i in range(1, len(s)):
            s1, s2 = s[:i], s[i:]
            if s1 in dict:
                s2Res = self.helper(s2, dict)
                for subRes in s2Res:
                    temp = [s1]
                    temp.extend(subRes)
                    res.append(temp)
        self.memo[s] = res
        return res

    def convertRes(self, res):
        return [" ".join(r) for r in res]



if __name__ == '__main__':
    s = Solution2().wordBreak
    res = s("leetcode", ["leet", "code"])
    print(res)

    a = "catsanddog"
    wordDict = ["cat", "cats", "and", "sand", "dog"]
    print(s(a, wordDict))


    a = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
    print(s(a, wordDict))
