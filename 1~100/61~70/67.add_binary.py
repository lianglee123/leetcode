class Solution:
    def addBinary(self, a: str, b: str) -> str:
        l = max(len(a), len(b))
        a = a.rjust(l, '0')
        b = b.rjust(l, '0')
        res = ''
        carry = '0'
        for i in range(l-1, -1, -1):
            a_char = a[i]
            b_char = b[i]
            one_count = (carry, a_char, b_char).count("1")
            if one_count == 0:
                carry, value = '0', '0'
            elif one_count == 1:
                carry, value = '0', '1'
            elif one_count == 2:
                carry, value = '1', '0'
            else:
                carry, value = '1', '1'
            res = value + res
        if carry != '0':
            res = carry + res
        return res





