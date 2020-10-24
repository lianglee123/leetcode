from typing import *
import math

class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while True:
            nextN = self.nextNumber(n)
            if nextN == 1:
                return True
            elif nextN in seen:
                return False
            else:
                seen.add(nextN)
            n = nextN

    def nextNumber(self, n):
        res = 0
        while n:
            n, r = divmod(n, 10)
            res += r**2
        return res


class Solution2:
    """
    快慢指针法
    类似单向链表判断是否有环的做法
    """
    def isHappy(self, n: int):
        if n == 1:
            return True
        slow = fast = n
        while True:
            slow = self.nextNumber(slow)
            fast = self.nextNumber(self.nextNumber(fast))
            if slow == 1 or fast == 1:
                return True
            elif slow == fast:
                return False

    def nextNumber(self, n):
        res = 0
        while n:
            n, r = divmod(n, 10)
            res += r**2
        return res



