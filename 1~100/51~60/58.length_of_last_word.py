
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if not s:
            return 0

        l = len(s) - 1
        i = l
        res = 0
        while i >= 0:
            if s[i] != " ":
                res += 1
            elif s[i] == " ":
                if res != 0:
                    return res
            i -= 1
        return res


if __name__ == '__main__':
    s = Solution().lengthOfLastWord
    print(s("  n  "))