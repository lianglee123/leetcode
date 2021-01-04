
class Solution:
    def grayCode(self, n):
        rs = [0]
        for i in range(n):
            j = len(rs) - 1
            while j >= 0:
                rs.append(rs[j] | (1 << i))
                j -= 1
        return rs

class Solution2:
    def grayCode(self, n):
        rs = [0]
        for i in range(n):
            j = len(rs) - 1
            a = 1 << i
            while j >= 0:
                rs.append(rs[j] + a)
                j -= 1
        return rs



def p_binary(vs):
    for v in vs:
        v = bin(v)[2:]
        if len(v) < 10:
            v = '0'*(10 - len(v)) + v
        print(v)


if __name__ == '__main__':
    s = Solution2().grayCode
    p_binary(s(5))


