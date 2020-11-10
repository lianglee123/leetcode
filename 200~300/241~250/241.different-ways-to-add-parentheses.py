from typing import *


class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        if input.isdigit():
            return [int(input)]
        res = []
        for i, c in enumerate(input):
            if c in ["+", "-", "*"]:
                left = self.diffWaysToCompute(input[:i])
                right = self.diffWaysToCompute(input[i+1:])
                for i in left:
                    for j in right:
                        if c == "+":
                            res.append(i+j)
                        elif c == '-':
                            res.append(i-j)
                        elif c == '*':
                            res.append(i*j)
                        else:
                            raise ValueError("wrong chra")
        return res

