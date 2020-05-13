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
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        cur = head
        count = 0
        while cur and count != k:
            cur = cur.next
            count += 1
        if count == k:
            cur = self.reverseKGroup(cur, k)
            while count > 0:
                temp = head.next
                head.next = cur
                cur = head
                head = temp
                count -= 1
            head = cur

        return head




if __name__ == '__main__':
    s = Solution().swapPairs
    r = s(Utils.array_to_node([1, 2, 3, 4, 5, 6]))
    Utils.print(r)
    r = s(Utils.array_to_node([1,]))
    Utils.print(r)
    r = s(Utils.array_to_node([1, 2]))
    Utils.print(r)
