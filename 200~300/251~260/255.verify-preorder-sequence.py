from typing import *

class Solution:
    def verifyPreOrder(self, preorder: List):
        if len(preorder) == 0:
            return True
        return self.helper(preorder, 0, len(preorder)-1)

    def helper(self, preorder: List, start: int, end: int):
        if start >= end or start + 1 == end:
            return True
        root = preorder[start]
        i = start + 1
        while i <= end:
            if preorder[i] > root:
                break
            i += 1
        return self.helper(preorder, start+1, i-1) and self.helper(preorder, i, end)


if __name__ == '__main__':
    s = Solution().verifyPreOrder
    print(s([5,4, 3, 4.5, 6, 5.5, 6.5]))
