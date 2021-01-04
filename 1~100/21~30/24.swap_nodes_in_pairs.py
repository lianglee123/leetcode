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
    def swapPairs(self, head: ListNode) -> ListNode:
        g = ListNode(next=head)
        ptr = g
        while ptr.next and ptr.next.next:
            ptr.next = self.swapFirstTwo(ptr.next)
            ptr = ptr.next.next
        return g.next


    def swapFirstTwo(self, node):
        h = node.next
        node.next.next, node.next = node, node.next.next
        return h


if __name__ == '__main__':
    s = Solution().swapPairs
    r = s(Utils.array_to_node([1, 2, 3, 4, 5, 6]))
    Utils.print(r)
    r = s(Utils.array_to_node([1,]))
    Utils.print(r)
    r = s(Utils.array_to_node([1, 2]))
    Utils.print(r)
