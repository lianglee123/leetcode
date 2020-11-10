from typing import *




class Solution:
    def __init__(self, words):
        self.dic = {}
        self.len = len(words)
        for i, w in enumerate(words):
            if w in self.dic:
                self.dic[w].append(i)
            else:
                self.dic[w] = [i]

    def shortestDistance(self, words, word1, word2):
        res = self.len
        i1 = 0
        i2 = 0
        d1 = self.dic[word1]
        d2 = self.dic[word2]
        while True:
            p1 = self.dic[word1]
            p2 = self.dic[word2]
            res = min(res, abs(p1-p2))
            if p1 < p2:
                i1 += 1
            else:
                i2 += 1
            if i1 >= len(d1)or i2 >= len(d2):
                break
        return res


