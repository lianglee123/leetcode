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
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if k == 0:
            return head
        l = self.length(head)
        if l == 0 or k % l == 0:
            return head
        print("l: ", l)
        k = l - (k % l) - 1
        print("k: ", k)
        cut_ptr = head
        while k > 0:
            cut_ptr = cut_ptr.next
            k -= 1
        print("cut point: ", cut_ptr.val)
        new_head = cut_ptr.next
        cut_ptr.next = None
        ptr = new_head
        while ptr and ptr.next:
            ptr = ptr.next
        ptr.next = head
        return new_head


    def length(self, head):
        l = 0
        while head != None:
            l += 1
            head = head.next
        return l


if __name__ == '__main__':
    s = Solution().rotateRight
    # head = Utils.array_to_node(range(1, 6))
    # Utils.print(head)
    # Utils.print(s(head, 2))

    # head = Utils.array_to_node(range(0, 3))
    # Utils.print(head)
    # Utils.print(s(head, 4))

    # head = Utils.array_to_node([1, 2])
    # Utils.print(head)
    # Utils.print(s(head, 1))

    head = Utils.array_to_node([1])
    Utils.print(head)
    Utils.print(s(head, 1))

    # head = Utils.array_to_node([1, 2])
    # Utils.print(head)
    # Utils.print(s(head, 0))
