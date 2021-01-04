import string

class Solution:
    """
    https://leetcode.com/problems/valid-number/discuss/23738/Clear-Java-solution-with-ifs
    """
    validNums = set(string.digits)
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        pointSeen = False
        eSeen = False
        numberSeen = False
        for i, c in enumerate(s):
            if c in self.validNums:
                numberSeen = True
            elif c == '.':
                if eSeen or pointSeen:
                    return False
                pointSeen = True
            elif c == 'e':
                if eSeen or (not numberSeen):
                    return False
                numberSeen = False
                eSeen = True
            elif c == '-' or c == '+':
                if i != 0 and s[i-1] != 'e':
                    return False
            else:
                return False
        return numberSeen