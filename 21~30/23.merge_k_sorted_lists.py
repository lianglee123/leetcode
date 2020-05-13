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
    """这种递归的实现方法真优雅"""
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        return self.partion(lists, 0, len(lists) - 1)

    def partion(self, lists, s, e):
        if s == e:
            return lists[s]
        if s < e:
            q = (s + e)//2
            l1 = self.partion(lists, s, q)
            l2 = self.partion(lists, q + 1, e)
            return self.mergeTwoLists(l1, l2)
        else:
            return None


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