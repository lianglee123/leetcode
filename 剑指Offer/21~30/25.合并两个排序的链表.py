from typing import *

class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next
    def __str__(self):
        return str(self.val) + "," + str(self.next)  if self.next else str(self.val)


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        guard = ListNode(0)
        ptr = guard
        while l1 and l2:
            if l1.val <= l2.val:
                ptr.next = l1
                l1 = l1.next
            else:
                ptr.next = l2
                l2 = l2.next
            ptr = ptr.next
        if l1:
            ptr.next = l1
        if l2:
            ptr.next = l2
        return guard.next


if __name__ == '__main__':
    n1 = ListNode(1, ListNode(3, ListNode(5)))
    n2 = ListNode(2, ListNode(4, ListNode(6)))
    s = Solution().mergeTwoLists
    print(s(n1, n2))



