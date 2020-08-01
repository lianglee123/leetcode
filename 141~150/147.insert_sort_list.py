class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return "%s --> %s" % (self.val, repr(self.next))


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        cur = head.next
        head.next = None
        while cur:
            node = cur
            cur = cur.next
            node.next = None
            head = self.insert(head, node)
        return head

    def insert(self, head, node):
        dummy = ListNode(0, head)
        pre = dummy
        cur = dummy.next
        while cur:
            if node.val <= cur.val:
                node.next = cur
                pre.next = node
                break
            else:
                pre, cur = cur, cur.next
        else:
            pre.next = node
            node.next = None
        return dummy.next


if __name__ == '__main__':
    a = ListNode(4, ListNode(2, ListNode(1, ListNode(3))))
    print(a)
    s = Solution().insertionSortList
    a = s(a)
    print(a)
