from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return "%s" % self.val

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
    """
    step1: find insert ptr
    step2: swap
    step3: stop in stop ptr
    """
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head or m == n:
            return head
        guard = ListNode(val='guard', next=head)

        # step1: find insert ptr
        insert_ptr = guard
        i = 1
        while i < m:
            insert_ptr = insert_ptr.next
            i += 1
        # print("insert ptr: ", insert_ptr.val)

        # step2: swap all after insert_ptr
        if not insert_ptr.next or not insert_ptr.next.next:
            return guard.next
        pre = insert_ptr.next
        cur = pre.next
        count = n - m   # step3: stop in specific count
        while cur and count:
            insert_ptr.next, pre.next, cur.next = cur, cur.next, insert_ptr.next
            cur = pre.next
            count -= 1
        return guard.next


if __name__ == '__main__':
    s = Solution().reverseBetween
    head = Utils.array_to_node([1, 2, 3, 4, 5])
    # Utils.print(s(head, 1, 2))
    Utils.print(s(head, 2, 5))
    # Utils.print(s(head, 3, 2))
    # Utils.print(s(head, 4, 2))
    # Utils.print(s(head, 1, 2))
    # s(head, 2, 2)
    # s(head, 3, 2)
    # s(head, 4, 2)
    # s(head, 5, 2)
    # s(head, 6, 2)
