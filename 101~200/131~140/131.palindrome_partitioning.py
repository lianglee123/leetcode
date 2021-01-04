from typing import *


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        self.dfs(res, [], s)
        return res
    def dfs(self, res, path, s):
        if not s:
            res.append(path[:])
        for i in range(1, len(s)+1):
            sub = s[:i]
            if self.isPalindrome(sub):
                path.append(sub)
                self.dfs(res, path, s[i:])
                path.pop()

    def isPalindrome(self, s):
        return s == s[::-1]


if __name__ == '__main__':
    from utils import *
    s = Solution().partition
    print(s("aab"))
