
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def sortList(self, head):
        if not head or not head.next:
            return head
        pre, slow, fast = None, head, head
        while fast and fast.next:
            pre, slow, fast = slow, slow.next, fast.next.next
        pre.next = None
        node1 = self.sortList(head)
        node2 = self.sortList(slow)
        return self.merge(node1, node2)

    def merge(self, node1, node2):
        dummy = tail = ListNode(0)
        ptr1 = node1
        ptr2 = node2
        while ptr1 and ptr2:
            if ptr1.val <= ptr2.val:
                littlePtr = ptr1
                ptr1 = ptr1.next
            else:
                littlePtr = ptr2
                ptr2 = ptr2.next
            tail.next = littlePtr
            tail = tail.next
        tail.next = ptr1 or ptr2
        return dummy.next
