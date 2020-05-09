from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        prefix = strs[0]
        for str in strs[1:]:
            if not str.startswith(prefix):
                prefix = self.longestPrefix(prefix, str)
                if not prefix:
                    break
        return prefix

    def longestPrefix(self, a: str, b: str) -> str:
        i = -1
        for c1, c2 in zip(a, b):
            if c1 != c2:
                break
            else:
                i += 1
        return a[:i+1]

