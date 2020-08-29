class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        slow = fast = head
        for i in range(k):
            if not fast:
                return None
            fast = fast.next
        while fast:
            fast = fast.next
            slow = slow.next
        return slow


if __name__ == '__main__':
    s = Solution().getKthFromEnd
    node = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
