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
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        resGuard = ListNode(val=0, next=head)
        resTail = resGuard.next
        ptr = head.next
        while ptr:
            if ptr.val != resTail.val:
                resTail.next = ptr
                resTail = ptr
            ptr = ptr.next
        resTail.next = None
        return resGuard.next


if __name__ == '__main__':
    s = Solution().deleteDuplicates
    Utils.print(s(Utils.array_to_node([1, 1, 2])))
    Utils.print(s(Utils.array_to_node([1, 1, 2, 3, 3])))
    Utils.print(s(Utils.array_to_node([1, 1, 2, 2])))
    Utils.print(s(Utils.array_to_node([1, 2, 2])))
    Utils.print(s(Utils.array_to_node([2, 2])))
