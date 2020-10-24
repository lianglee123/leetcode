

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if not s and not t:
            return True
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s.index(s[i]) != t.index(t[i]):
                return False
        return True


