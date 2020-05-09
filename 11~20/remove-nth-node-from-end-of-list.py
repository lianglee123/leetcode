class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        sentry = ListNode(val=0, next=head)
        fast_ptr = sentry
        slow_ptr = sentry
        for i in range(n):
            fast_ptr = fast_ptr.next
        while fast_ptr:
            fast_ptr = fast_ptr.next
            slow_ptr = slow_ptr.next
        slow_ptr.next = slow_ptr.next.next
        return sentry.next

