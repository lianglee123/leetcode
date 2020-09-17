from typing import *



class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = [(-1, float('inf'))]

    def push(self, x: int) -> None:
        self.stack.append((x, min(x, self.stack[-1][1])))

    def pop(self) -> int:
        if len(self.stack) > 1:
            return self.stack.pop()[0]
        else:
            raise IndexError("pop from empty list")


    def top(self) -> int:
        if len(self.stack) == 1:
            return None
        return self.stack[-1][0]

    def getMin(self) -> int:
        if len(self.stack) > 1:
            return self.stack[-1][1]
        else:
            raise ValueError("stack is empty")


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()