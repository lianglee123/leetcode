from typing import *


from collections import defaultdict


class Solution:
    def canPermutePalindrome(self, s):
        countMap = defaultdict(int)
        for c in s:
            countMap[c] += 1
        oneCount = 0
        for k, v in countMap:
            if v == 1:
                oneCount += 1
                if oneCount > 1:
                    return False
            elif v == 2:
                continue
            else:
                return False

class Solution1:
    def canPermutePalindrome(self, s):
        seen = {}
        for c in s:
            if c in seen:
                del seen[c]
            else:
                seen[c] = True
        return not seen or len(seen) == 1




