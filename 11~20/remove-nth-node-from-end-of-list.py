from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Utils:
    @staticmethod
    def array_to_node(values: List):
        sentry = ListNode()
        ptr = sentry
        for v in values:
            ptr.next = ListNode(v)
            ptr = ptr.next
        return sentry.next

    @staticmethod
    def node_to_array(node: ListNode):
        if not node:
            return None
        res = []
        while node:
            res.append(node.val)
            node = node.next
        return res

    @staticmethod
    def print(node):
        print(Utils.node_to_array(node))



class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        sentry = ListNode(val=0, next=head)
        fast_ptr = sentry
        slow_ptr = sentry
        for i in range(n+1):
            fast_ptr = fast_ptr.next
        while fast_ptr:
            fast_ptr = fast_ptr.next
            slow_ptr = slow_ptr.next
        slow_ptr.next = slow_ptr.next.next
        return sentry.next


class Solution2:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy
        for _ in range(0, n):
            first = first.next
        while first.next:   # Solution1和Sulution2的区别在这
            second = second.next
            first = first.next

        tmp = second.next
        second.next = tmp.next
        tmp.next = None
        return dummy.next


if __name__ == '__main__':
    s = Solution().removeNthFromEnd
    node = Utils.array_to_node([1, 2, 3, 4, 5])
    Utils.print(s(node, 2))