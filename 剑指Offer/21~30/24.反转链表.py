from typing import *

class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next
    def __str__(self):
        return str(self.val) + "," + str(self.next)  if self.next else str(self.val)


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre, cur = None, head
        while cur:
            temp = cur.next
            cur.next = pre
            pre, cur = cur, temp
        return pre


if __name__ == '__main__':
    n = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    print(Solution().reverseList(n))
    print(Solution().reverseList(ListNode(1, ListNode(2,))))
    print(Solution().reverseList(ListNode(1)))


