from typing import *


from collections import defaultdict


class Solution:
    def canPermutePalindrome(self, s):
        countMap = defaultdict(int)
        for c in s:
            countMap[c] += 1
        oneChar = ''
        twoChars = []
        for k, v in countMap:
            if v == 1:
                if oneChar != "":
                    return []
                oneChar = k
            elif v == 2:
                twoChars.append(k)
            else:
                return []
        pers = []
        self.permutation(pers, 0, twoChars)
        return [p + oneChar for p in pers]

    def permutation(self, res, position, chars: List):
        """
        这个全排列的思想是，固定住第一个元素，对剩余的元素进行全排列
        https://blog.csdn.net/qq_31601743/article/details/82053201
        """
        if position == len(chars):
            res.append('.'.join(chars))
            return
        for i in range(position, len(chars)):
            chars[i], chars[position] = chars[position], chars[i]
            self.permutation(res, position + 1, chars)
            chars[i], chars[position] = chars[position], chars[i]

