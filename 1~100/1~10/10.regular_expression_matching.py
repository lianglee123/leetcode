from functools import lru_cache


class Solution:
    """
    使用f(i,j), 表示s[:i+1], p[:j+1]是否匹配，
    如果没有*， 那么，f(i, j) = f(i-1, j-1) And S[i] == P[j]
    如果有*, 感觉就违背了dp的无后效性：过去的不影响将来，将来的不影响过去。
    所以还是这种递归做法最简单，但是这种递归一眼可以总结出DP,因为有重复子自问题
    """
    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return not s
        first_match = bool(s) and (p[0]=='.' or s[0]==p[0])

        if len(p) > 1 and p[1] == "*":
            return self.isMatch(s, p[2:]) or (first_match and self.isMatch(s[1:], p))
        else:
            return first_match and self.isMatch(s[1:], p[1:])

from typing import List


class Solution2:
    """
    给Solution加上cache
    排名： 排名99.49%
    使用f(i,j), 表示s[:i+1], p[:j+1]是否匹配，
    如果没有*， 那么，f(i, j) = f(i-1, j-1) And S[i] == P[j]
    如果有*, 感觉就违背了dp的无后效性：过去的不影响将来，将来的不影响过去。
    所以还是这种递归做法最简单，但是这种递归一眼可以总结出DP,因为有重复子自问题
    """
    def isMatch(self, s: str, p: str) -> bool:
        cache = [[None] * (len(p) + 1) for _ in range(len(s)+1)]
        print(cache)
        return self.__isMatch(s, p, cache)

    def __isMatch(self, s: str, p: str, cache: List[List[bool]]) -> bool:
        print(s, p)
        if cache[len(s)][len(p)] is not None:
            return cache[len(s)][len(p)]
        if not p:
            res = not s
        else:
            first_match = bool(s) and (p[0]=='.' or s[0]==p[0])

            if len(p) > 1 and p[1] == "*":
                res = self.__isMatch(s, p[2:], cache) or (first_match and self.__isMatch(s[1:], p, cache))
            else:
                res = first_match and self.__isMatch(s[1:], p[1:], cache)
        cache[len(s)][len(p)] = res
        return res


if __name__ == '__main__':
    s = Solution2().isMatch
    print(s("aa", "a*"))