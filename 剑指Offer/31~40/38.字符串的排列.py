from typing import *

from collections import deque

class Solution:
    def permutation(self, s: str) -> List[str]:
        res = set()
        self.dfs(s, [], deque(s), res)
        return list(res)

    def dfs(self, s, path, charDeque, res):
        if len(path) == len(s):
            res.add("".join(path))
        else:
            for _ in range(len(charDeque)):
                temp = charDeque.pop()
                path.append(temp)
                self.dfs(s, path, charDeque, res)
                path.pop()
                charDeque.appendleft(temp)


if __name__ == '__main__':
    s = Solution().permutation
    print(s("abc"))
    print(s("aab"))
