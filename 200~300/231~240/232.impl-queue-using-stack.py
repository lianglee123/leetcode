from typing import *


class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stx1 = []
        self.stx2 = []


    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stx1.append(x)


    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
            """
        if self.stx2:
            return self.stx2.pop()
        while self.stx1:
            self.stx2.append(self.stx1.pop())
        return self.stx2.pop()



    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.stx2:
            return self.stx2[-1]
        while self.stx1:
            self.stx2.append(self.stx1.pop())
        return self.stx2[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.stx1 and not self.stx2


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()