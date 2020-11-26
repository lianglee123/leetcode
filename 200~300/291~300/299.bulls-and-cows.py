from typing import *



from collections import defaultdict


class Solution:
    """
    https://blog.csdn.net/fuxuemingzhu/article/details/82872065
    """
    def getHint(self, secret, guess):
        bulls = 0
        cows = 0
        secretDic = defaultdict(int)
        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1
            else:
                secretDic[s] += 1
        for i, g in enumerate(guess):
            if secret[i] != guess[i] and secretDic[g]:
                cows += 1
                secretDic[g] -= 1
        return str(bulls) + "A" + str(cows) + "B"



