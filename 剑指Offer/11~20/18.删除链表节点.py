from typing import *


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return str(self.val) + "," + str(self.next)

class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        guard = ListNode(None)
        guard.next = head
        cur = guard
        while cur and cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
                return guard.next
            else:
                cur = cur.next
        return guard.next

class Solution2:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        cur = head
        if cur.val == val:
            return cur.next

        while cur and cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head


if __name__ == '__main__':
    n4 = ListNode(4)
    n5 = ListNode(5)
    n1 = ListNode(1)
    n9 = ListNode(9)

    n4.next = n5
    n5.next = n1
    n1.next = n9
    print(n4)
    s = Solution().deleteNode

    print(s(n4, 9))
