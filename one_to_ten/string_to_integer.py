class Solution:
    MAX = 2**31 -1
    MIN = -2**31

    def myAtoi(self, str: str) -> int:
        number_str = self.read_number_str(str)
        if (not number_str):
            return 0
        res = int(number_str)
        if res > Solution.MAX:
            return Solution.MAX
        elif res < Solution.MIN:
            return Solution.MIN
        else:
            return res

    def read_number_str(self, str: str):
        str = str.lstrip()
        a = ''
        if str.startswith("-") or str.startswith("+"):
            a = str[0]
            str = str[1:]
        for c in str:
            if c in ('0123456789'):
                a += c
            else:
                break
        if a == "+" or a == "-":
            return ''
        return a