from typing import *


class Solution:

    def wordPatternMatch(self, pattern, words):
        patternMap = {}
        seenWords = set()
        return self.helper(pattern, words, p, r, patternMap, seenWords)

    def helper(self, pattern, words, p, r, patternMap, seenWords: Set):
        if p == len(pattern) and r == len(words):
            return True
        if p == len(pattern) or r == len(words):
            return False
        c = pattern[p]
        for i in range(r, len(pattern)):
            word = words[r:i-r+1]
            if c in patternMap and word == patternMap[c]:
                if self.helper(pattern, words, p+1, i+1, patternMap, seenWords):
                    return True
            elif c not in patternMap:
                if word not in seenWords:
                    patternMap[c] = word
                    seenWords.add(word)
                    if self.helper(pattern, words, p+1, i+1, patternMap, seenWords):
                        return True
                    del patternMap[c]
                    seenWords.remove(word)

        return False