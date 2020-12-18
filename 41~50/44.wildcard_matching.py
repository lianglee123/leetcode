from typing import List


class Solution:
    """
    Time Limit Exceeded Answer
    第二遍评注：
        这里的for range其实可以去除，使用彻底的递归代替：
        self.isMatch(s, p[1:]) or self.isMatch(s[1:], p))
        (星星一个字符都不匹配) or （星星匹配一个字符并继续递归）
        如下SolutionTwice
    """
    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return not s
        if p[0] == '?':
            if len(s) > 0:
                return self.isMatch(s[1:], p[1:])
            else:
                return False
        elif p[0] == '*':
            for i in range(len(s)+1):
                print("---> i: ", i, s[i:], p[1:])
                if self.isMatch(s[i:], p[1:]):
                    return True
        else:
            if len(s) > 0:
                return p[0] == s[0] and self.isMatch(s[1:], p[1:])
            else:
                return False



class Solution2:
    """
    Time Limit Exceeded Answer
    """

    def isMatch(self, s: str, p: str) -> bool:
        return self._isMatch([i for i in s], [i for i in p])

    def _isMatch(self, s: List[str], p: List[str]) -> bool:
        if not p:
            return not s
        if p[0] == '?':
            if len(s) > 0:
                return self._isMatch(s[1:], p[1:])
            else:
                return False
        elif p[0] == '*':
            for i in range(len(s)+1):
                if self._isMatch(s[i:], p[1:]):
                    return True
        else:
            if len(s) > 0:
                return p[0] == s[0] and self._isMatch(s[1:], p[1:])
            else:
                return False


class SolutionFiniteStateMachine:
    """
    不理解的答案
    """
    def isMatch(self, s, p):
        transfer = {}
        state = 0
        for char in p:
            if char == '*':
                transfer[(state, char)] = state
            else:
                transfer[(state, char)] = state + 1
                state += 1
        accept = state
        states = {0,}
        for char in s:
            _states = set()
            for token in [char, '*', '?']:
                for at in states:
                    next_state = transfer.get((at, token))
                    if next_state is not None:
                        _states.add(next_state)
            states = _states
        return accept in state


class SolutionTwice:
    """
    然后再加上Cache
    """
    def isMatch(self, s, p):
        if not p:
            return not s
        if p[0] == '?':
            return bool(s) and self.isMatch(s[1:], p[1:])
        elif p[0] == '*':
            # 星星一个字符都不匹配 或者 只匹配一个字符并继续递归
            return (self.isMatch(s, p[1:])) or (bool(s) and self.isMatch(s[1:], p))
        else:
            return bool(s) and p[0] == s[0] and self.isMatch(s[1:], p[1:])

from functools import lru_cache


class SolutionTwice2:
    """
    加上了字典Cache执行时间排名为7.86%
    """
    def isMatch(self, s, p):

        return self.__isMatch(s, p, {})

    def __isMatch(self, s, p, cache):
        if (s, p) in cache:
            return cache[(s, p)]
        if not p:
            res = not s
        elif p[0] == '?':
            res = bool(s) and self.__isMatch(s[1:], p[1:], cache)
        elif p[0] == '*':
            # 星星一个字符都不匹配 或者 只匹配一个字符并继续递归
            res = self.__isMatch(s, p[1:], cache) or (bool(s) and self.__isMatch(s[1:], p, cache))
        else:
            res = bool(s) and p[0] == s[0] and self.__isMatch(s[1:], p[1:], cache)
        cache[(s, p)] = res
        return res


class SolutionTwice3:
    """
    加上了字典Cache执行时间排名为7.86%
    使用列表的cache排名84%
    """
    def isMatch(self, s, p):
        cache = [[None] * (len(p)+1)
                 for _ in range(len(s) + 1)]
        return self.__isMatch(s, p, cache)

    def __isMatch(self, s, p, cache):
        if cache[len(s)][len(p)] is not None:
            return cache[len(s)][len(p)]
        if not p:
            res = not s
        elif p[0] == '?':
            res = bool(s) and self.__isMatch(s[1:], p[1:], cache)
        elif p[0] == '*':
            # 星星一个字符都不匹配 或者 只匹配一个字符并继续递归
            res = self.__isMatch(s, p[1:], cache) or (bool(s) and self.__isMatch(s[1:], p, cache))
        else:
            res = bool(s) and p[0] == s[0] and self.__isMatch(s[1:], p[1:], cache)
        cache[len(s)][len(p)] = res
        return res


if __name__ == '__main__':
    s = SolutionTwice3().isMatch
    # assert s("aa", "a") == False
    # assert s("aa", "*") == True
    # assert s("adceb", "*a*b") == True
    # assert s("acdcb", "a*c?b") == False
    # assert s("", "*") == True
    # assert s("aa", "*") == True
    # assert s("cb", "?a") == False
    assert s("aaabbbaabaaaaababaabaaabbabbbbbbbbaabababbabbbaaaaba",
             "a*******b") == False