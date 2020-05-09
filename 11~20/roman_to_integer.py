class Solution:
    def romanToInt(self, s: str) -> int:
        integers = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        romans = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        res = 0
        i = 0
        while s:
            if s[:2] in romans[i:]:
                roman = s[:2]
                s = s[2:]
                i = romans.index(roman)
                res += integers[i]
            elif s[0] in romans[i:]:
                roman = s[0]
                s = s[1:]
                i = romans.index(roman)
                res += integers[i]
            else:
                raise ValueError("wrong s")

        return res


class Solution2:
    def romanToInt(self, s: str) -> int:
        if not s:
            return 0
        integers = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        romans = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        res = 0
        i = 0
        l = len(s)
        s_i = 0
        while s_i < l:
            if s[s_i:s_i+2] in romans[i:]:
                roman = s[s_i:s_i+2]
                s_i += 2
                i = romans.index(roman)
                res += integers[i]
            elif s[s_i:s_i+1] in romans[i:]:
                roman = s[s_i:s_i+1]
                s_i += 1
                i = romans.index(roman)
                res += integers[i]
            else:
                raise ValueError("wrong s")

        return res
