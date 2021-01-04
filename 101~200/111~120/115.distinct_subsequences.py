from functools import lru_cache


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if not t or not s:
            return 0
        return self._numDistinct(s, t)

    @lru_cache(maxsize=10000)
    def _numDistinct(self, s: str, t: str) -> int:
        if not t:
            return 1
        if not s:
            return 0
        if s[0] == t[0]:
            return self._numDistinct(s[1:], t[1:]) + self._numDistinct(s[1:], t)
        else:
            return self._numDistinct(s[1:], t)


if __name__ == '__main__':
    s = "babgbag"
    t = "bag"
    print(Solution()._numDistinct(s, t))
    print(Solution()._numDistinct("rabbbit", "rabbit"))
    print(Solution()._numDistinct("aabdbaabeeadcbbdedacbbeecbabebaeeecaeabaedadcbdbcdaabebdadbbaeabdadeaabbabbecebbebcaddaacccebeaeedababedeacdeaaaeeaecbe",
                                  "bddabdcae"))

