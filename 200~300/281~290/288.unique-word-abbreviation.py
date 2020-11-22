from typing import *

from collections import defaultdict

class Solution:

    def __init__(self, dic: List[str]):
        self.dic = dic
        self.abbrDic = defaultdict(int)
        for w in dic:
            self.abbrDic[self.abbr(w)] += 1

    def abbr(self, word):
        if len(word) <= 2:
            return word
        else:
            return word[0] + str(len(word) - 2) + word[-1]

    def isUnique(self, word):
        if  word not in self.dic:
            return True
        return self.abbrDic[self.abbr(word)] <= 1





