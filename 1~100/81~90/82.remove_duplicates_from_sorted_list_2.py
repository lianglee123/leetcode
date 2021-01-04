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
    """
    递归法
    """
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        ptr = head
        while ptr.next:
            if ptr.next.val == ptr.val:
                ptr = ptr.next
            else:
                break
        if ptr == head:
            head.next = self.deleteDuplicates(ptr.next)
        else:
            head = self.deleteDuplicates(ptr.next)
        return head


class Solution2:
    """
    遍历法，，迭代找出所有distinct的ListNode, 加入新节点。
    """
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        resGuard = ListNode()
        resTail = resGuard
        ptr = head
        while ptr:
            temp = ptr
            while ptr.next and ptr.next.val == ptr.val:
                ptr = ptr.next
            if ptr == temp:  # distinct
                resTail.next = ptr
                resTail = ptr
            ptr = ptr.next
        resTail.next = None
        return resGuard.next



if __name__ == '__main__':
    s = Solution2().deleteDuplicates
    head = Utils.array_to_node([1, 2, 3, 3, 4, 4, 5])
    Utils.print(s(head))

    head = Utils.array_to_node([1, 1, 1, 2, 3])
    Utils.print(s(head))

    head = Utils.array_to_node([1, 2, 2])
    Utils.print(s(head))
    head = Utils.array_to_node([1, 1, 2, 2])
    Utils.print(s(head))
    head = Utils.array_to_node([1, 1, 1, 1])
    Utils.print(s(head))
