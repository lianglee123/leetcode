from typing import *


class Solution:

    def wordPattern(self, pattern, wordsStr):
        words = wordsStr.strip().split(" ")
        if len(words) != pattern:
            return False

        patternDic = {}
        seedWords = set()
        for i, c in enumerate(pattern):
            if c in pattern:
                if words[i] != patternDic[c]:
                    return False
            else:
                if words[i] not in seedWords:
                    patternDic[c] = words[i]
                    seedWords.add(words[i])
                else:
                    return False
        return True


