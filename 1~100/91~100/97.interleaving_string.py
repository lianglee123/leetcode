from functools import lru_cache

class Solution:
    """
    python 字符串 not slice by reference， 所以需要优化
    https://stackoverflow.com/questions/5722006/does-python-do-slice-by-reference-on-strings#:~:text=2%20Answers&text=Python%20does%20slice%2Dby%2Dcopy,into%20a%20new%20string%20object.&text=With%20the%20slice%2Das%2Dcopy,string%20a%20is%20immediately%20freed.
    """

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        if not s1:
            return s3 == s2
        if not s2:
            return s3 == s1
        if not s3:
            return False

        c = s3[0]
        if c == s1[0] and c == s2[0]:
            return self.isInterleave(s1[1:], s2, s3[1:]) or self.isInterleave(s1, s2[1:], s3[1:])
        elif c == s1[0]:
            return self.isInterleave(s1[1:], s2, s3[1:])
        elif c == s2[0]:
            return self.isInterleave(s1, s2[1:], s3[1:])
        else:
            return False


class Solution2:
    """
    python 字符串 not slice by reference， 所以需要优化
    https://stackoverflow.com/questions/5722006/does-python-do-slice-by-reference-on-strings#:~:text=2%20Answers&text=Python%20does%20slice%2Dby%2Dcopy,into%20a%20new%20string%20object.&text=With%20the%20slice%2Das%2Dcopy,string%20a%20is%20immediately%20freed.

    但是这种优化，算法复杂度依然时2**n
    """

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        if not s1:
            return s3 == s2
        if not s2:
            return s3 == s1
        return self.h(s1, s2, s3, 0, 0, 0)

    @lru_cache()
    def h(self, s1, s2, s3, i1, i2, i3) -> bool:
        # print(i1, i2, i3)
        if i3 == len(s3):
            return i1 == len(s1) and i2 == len(s2)

        c = s3[i3]
        if i1 < len(s1) and i2 < len(s2) and c == s1[i1] and c == s2[i2]:
            return self.h(s1, s2, s3, i1+1, i2, i3+1) or self.h(s1, s2, s3, i1, i2+1, i3+1)
        elif i1 < len(s1) and c == s1[i1]:
            return self.h(s1, s2, s3, i1+1, i2, i3+1)
        elif  i2 < len(s2) and c == s2[i2]:
            return self.h(s1, s2, s3, i1, i2+1, i3+1)
        else:
            return False


if __name__ == '__main__':
    s = Solution2().isInterleave
    # s1 = "aabcc"
    # s2 = "dbbca"
    # s3 = "aadbbcbcac"
    #
    # print(s(s1, s2, s3))

    s1 = "bbbbbabbbbabaababaaaabbababbaaabbabbaaabaaaaababbbababbbbbabbbbababbabaabababbbaabababababbbaaababaa"
    s2 = "babaaaabbababbbabbbbaabaabbaabbbbaabaaabaababaaaabaaabbaaabaaaabaabaabbbbbbbbbbbabaaabbababbabbabaab"
    s3 = "babbbabbbaaabbababbbbababaabbabaabaaabbbbabbbaaabbbaaaaabbbbaabbaaabababbaaaaaabababbababaababbababbbababbbbaaaabaabbabbaaaaabbabbaaaabbbaabaaabaababaababbaaabbbbbabbbbaabbabaabbbbabaaabbababbabbabbab"
    print(s(s1, s2, s3))


