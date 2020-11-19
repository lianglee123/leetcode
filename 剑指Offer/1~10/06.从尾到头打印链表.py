from typing import List

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
"""
思路是先遍历收集值，然后再反转。

变种：要求直接的返回逆序？使用stack, 但是空间复杂度依然是O(N)
"""
class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        res = []
        while head:
            res.append(head.val)
            head = head.next
        return res[::-1]
