from typing import *

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head):
        if not head or not head.next:
            return head
        pre = None
        cur = head
        while cur:
            tmp = cur.next
            cur.next = pre
            pre, cur = cur, tmp
        return pre


class Solution2:
    def reverseList(self, head):
        if not head or not head.next:
            return head
        a = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return a




if __name__ == '__main__':
    from utils.list_node_utils import Utils
    s = Solution().reverseList
    n = Utils.array_to_node([1, 2, 3, 4, 5])
    Utils.print(s(n))