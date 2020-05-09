from typing import List


class Solution:
    digit_map = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z'],
    }
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return Solution.digit_map[digits]
        res = []
        for s in self.letterCombinations(digits[1:]):
            for c in Solution.digit_map[digits[0]]:
                res.append(c + s)
        return res



if __name__ == '__main__':
    s = Solution().letterCombinations
    print(s("23456"))