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
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        guard = ListNode()
        ptr = guard

        while l1 or l2:
            if not l1:
                ptr.next = l2
                return guard.next
            if not l2:
                ptr.next = l1
                return guard.next
            if l1.val <= l2.val:
                ptr.next = l1
                ptr = ptr.next
                l1 = l1.next
            else:
                ptr.next = l2
                ptr = ptr.next
                l2 = l2.next
        return guard.next


if __name__ == '__main__':
    s = Solution().mergeTwoLists
    r = s(Utils.array_to_node([1, 2, 4]), Utils.array_to_node([1, 3, 4]))
    Utils.print(r)