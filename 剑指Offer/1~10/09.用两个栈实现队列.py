from typing import *


class CQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []


    def appendTail(self, value: int) -> None:
        self.stack1.append(value)

    def deleteHead(self) -> int:
        if self.stack2:
            return self.stack2.pop()
        else:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            return self.stack2.pop() if self.stack2 else -1


class CQueue2:
    """
    这是一个错误实现，理解这个实现错在哪里，才算理解了这个题。
    """
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def appendTail(self, value: int) -> None:
        self.stack1.append(value)

    def deleteHead(self) -> int:
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        return self.stack2.pop() if self.stack2 else -1


if __name__ == '__main__':
    obj = CQueue()
    obj.appendTail(1)
    obj.appendTail(2)
    obj.appendTail(3)
    print(obj.deleteHead())
    print(obj.deleteHead())
    print(obj.deleteHead())
    print(obj.deleteHead())