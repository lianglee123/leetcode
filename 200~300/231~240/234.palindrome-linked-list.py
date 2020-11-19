from typing import *


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None



class Solution:
    def isPalindrome(self, head) -> bool:
        values = []
        while head:
            values.append(head.val)
            head = head.next
        return values == values[::-1]
