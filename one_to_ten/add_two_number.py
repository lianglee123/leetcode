from typing import List

# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def array_to_node(array: List[int]) -> ListNode:
    head = ListNode()
    ptr = head
    for n in array:
        ptr.next = ListNode(n)
        ptr = ptr.next
    return head.next


def node_to_array(node: ListNode) -> ListNode:
    if node is None:
        return None
    res = []
    while node:
        res.append(node.val)
        node = node.next
    return res

"""
这道题我反复改了几次才通过测试
以下几项要格外注意：
1. l1或l2为空时，carry依然可能有值
2. l1和l2都为空时，carry依然可能有值
"""

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        res_header = ListNode(0)
        ptr = res_header
        while l1 and l2:
            val = l1.val + l2.val + carry
            if val >= 10:
                carry = 1
                val = val - 10
            else:
                carry = 0
            ptr.next = ListNode(val)
            ptr = ptr.next
            l1 = l1.next
            l2 = l2.next

        while l1:
            val = l1.val + carry
            if val >= 10:
                carry = 1
                val = val - 10
            else:
                carry = 0
            ptr.next = ListNode(val)
            ptr = ptr.next
            l1 = l1.next

        while l2:
            val = l2.val + carry
            if val >= 10:
                carry = 1
                val = val - 10
            else:
                carry = 0
            ptr.next = ListNode(val)
            ptr = ptr.next
            l2 = l2.next

        if carry:
            ptr.next = ListNode(carry)

        return res_header.next


class Solution2:
    """
    把几个循环合并处理
    """
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        res_header = ListNode(0)
        ptr = res_header
        while (l1 or l2 or carry):
            if l1:
                l1_val = l1.val
                l1 = l1.next
            else:
                l1_val = 0

            if l2:
                l2_val = l2.val
                l2 = l2.next
            else:
                l2_val = 0

            val = l1_val + l2_val + carry
            if val >= 10:
                carry = 1
                val = val - 10
            else:
                carry = 0

            ptr.next = ListNode(val)
            ptr = ptr.next

        return res_header.next


if __name__ == '__main__':
    s = Solution2()
    l1 = array_to_node([1])
    l2 = array_to_node([9, 9])
    print(node_to_array(s.addTwoNumbers(l1, l2)))
    assert node_to_array(s.addTwoNumbers(l1, l2)) == [0, 0, 1]
