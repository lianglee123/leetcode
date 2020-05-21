from typing import List


class Solution:
    """
    Time Limit Exceeded Ansomer
    """
    def isMatch(self, s: str, p: str) -> bool:
        print("isMatch: ", s, p)
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
    Time Limit Exceeded Ansomer
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


if __name__ == '__main__':
    s = Solution2().isMatch
    # assert s("aa", "a") == False
    # assert s("aa", "*") == True
    # assert s("adceb", "*a*b") == True
    # assert s("acdcb", "a*c?b") == False
    # assert s("", "*") == True
    assert s("aa", "*") == True