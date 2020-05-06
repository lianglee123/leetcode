from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def my_assert(val, expect):
    if val == expect:
        return
    else:
        raise AssertionError("%s not equal %s", val, expect)
