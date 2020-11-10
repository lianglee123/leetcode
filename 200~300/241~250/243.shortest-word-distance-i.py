from typing import *



class Solution:
    def shortestDistance(self, words, word1, word2):
        p1 = -1
        p2 = -1
        res = len(words)
        for i, w in enumerate(words):
            if w == word1:
                p1 = i
            elif w == word2:
                p2 = i
            if p1 != -1 and p2 != -1:
                res = min(res, abs(p1-p2))
        return res



