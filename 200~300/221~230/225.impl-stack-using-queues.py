from typing import *

from collections import  deque


class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1 = deque()
        self.q2 = deque()


    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        Push时，先把q1原有的元素放到q2中临时中转，
        等到把元素推到q1中之后，再把原有的元素推回到q1中
        这里有两个周转操作，我们可以通过交换q1和q2,减少到一个周转操作
        q2永远为空
        """
        self.q2.append(x)
        while self.q1:
            self.q2.appendleft(self.q1.pop())
        self.q1, self.q2 = self.q2, self.q1

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.q1.pop()

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.q1[-1]


    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not self.q1

if __name__ == '__main__':

    # Your MyStack object will be instantiated and called as such:
    obj = MyStack()
    obj.push(1)
    obj.push(2)
    param_2 = obj.pop()
    param_3 = obj.top()
    param_4 = obj.empty()
    print(param_2, param_3, param_4)