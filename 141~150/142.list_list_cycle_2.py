class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head:
            return None

        walker = head
        runner = head
        while runner.next and runner.next.next:
            walker = walker.next
            runner = runner.next.next
            if walker == runner:
                newWalker = head
                while walker != newWalker:
                    newWalker = newWalker.next
                    walker = walker.next
                else:
                    return newWalker

        return None

