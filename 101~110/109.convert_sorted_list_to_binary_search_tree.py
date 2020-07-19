class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import *


class Solution:
    def sortedListToBST(self, head):
        if not head:
            return None
        return self.toBST(head, None)

    def toBST(self, head, tail):
        slow = head
        fast = head
        if head == tail:
            return None
        while fast != tail and fast.next != tail:
            fast = fast.next.next
            slow = slow.next
        thead = TreeNode(slow.val)
        thead.left = self.toBST(head,slow)
        thead.right = self.toBST(slow.next,tail)
        return thead
