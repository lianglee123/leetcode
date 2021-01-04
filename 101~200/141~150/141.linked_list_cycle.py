# public class Solution {
# public boolean hasCycle(ListNode head) {
# if(head==null) return false;
# ListNode walker = head;
# ListNode runner = head;
# while(runner.next!=null && runner.next.next!=null) {
# walker = walker.next;
# runner = runner.next.next;
# if(walker==runner) return true;
# }
# return false;
#
# }
# }


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False
        walker = head
        runner = head
        while runner.next and runner.next.next:
            walker = walker.next
            runner = runner.next.next
            if walker == runner:
                return True
        return False

