from typing import *


class Solution:
    """
    https://www.cnblogs.com/Dylan-Java-NYC/p/5186278.html
    """
    def generatePossibleNextMoves(self, s):
        res = []
        for i in range(1, len(s)):
            if s[i] == '+' and s[i-1] == '+':
                res.append(s[0:i-1] + "--" + s[i+1:])
        return res




