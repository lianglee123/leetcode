from typing import *


class Solution:
    """
    https://www.cnblogs.com/grandyang/p/5192426.html
    """
    def shortestDistance(self, words, word1, word2):
        p1 = -1
        p2 = -1
        res = len(words)
        wEq = word1 == word2

        for i, w in enumerate(words):
            t = p1
            if w == word1:
                p1 = i
            if w == word2:
                p2 = i
            if p1 != -1 and p2 != -1:
                if wEq and t != -1 and t != p1:
                    res = min(res, abs(t - p1))
                elif p1 != p2:
                    res = min(res, abs(p1-p2))
        return res


