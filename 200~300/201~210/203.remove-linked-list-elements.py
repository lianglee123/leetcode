from typing import *


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        guard = ListNode(None)
        guard.next = head
        pre = guard
        cur = guard.next
        while cur:
            if cur.val == val:
                tmp = cur.next
                pre.next = tmp
                cur = tmp

            else:
                pre, cur = cur, cur.next
        return guard.next
