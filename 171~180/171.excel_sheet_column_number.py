class Solution:
    def titleToNumber(self, s: str) -> int:
        if not s:
            return 0
        convert = lambda c: ord(c) - 64
        res = 0
        for i, c in enumerate(s[::-1]):
            weight = 26 ** i
            res += convert(c) * weight
        return res


if __name__ == '__main__':
    s = Solution().titleToNumber
    print(s("A"))
    print(s("Z"))
    print(s("AB"))





