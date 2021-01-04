from typing import *

import string

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if not tokens:
            raise ValueError("token is empty")
        validOperators = '+-*/'
        stack = []
        while tokens:
            t = tokens.pop(0)
            if t in validOperators:
                n1 = stack.pop()
                n2 = stack.pop()
                if t == "*":
                    stack.append(n1 * n2)
                elif t == "+":
                    stack.append(n1 + n2)
                elif t == "-":
                    stack.append(n2 - n1)
                elif t == "/":
                    stack.append(int(n2 / n1))
                else:
                    raise ValueError("unReached")
            elif self.isDigit(t):
                stack.append(int(t))
            else:
                raise ValueError("wrong token")
        return stack.pop()

    def isDigit(self, s: str):
        return s.isdigit() or (s.startswith("-") and s[1:].isdigit())

if __name__ == '__main__':
    s = Solution().evalRPN
    print(s(["2", "1", "+", "3", "*"]))
    print(s(["4", "13", "5", "/", "+"]))
    print(s(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
