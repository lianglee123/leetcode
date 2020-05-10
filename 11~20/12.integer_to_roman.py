from collections import OrderedDict

class Solution:
    def intToRoman(self, num: int) -> str:
        if not num:
            return ""
        integers = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        romans = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        res = ""
        i = 0
        while num:
            if num >= integers[i]:
                roman = romans[i]
                num -= integers[i]
                res += roman
            else:
                i += 1
        return res


if __name__ == '__main__':
    s = Solution().intToRoman
    print(s(1000))