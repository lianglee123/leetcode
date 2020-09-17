from typing import *




class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        if not postorder:
            return True
        return self.helper(postorder, 0, len(postorder)-1)

    def helper(self, postorder, s, e):
        if s >= e:
            return True
        i = s
        while postorder[i] < postorder[e]:
            i += 1
        m = i
        while postorder[i] > postorder[e]:
            i += 1
        return i == e and self.helper(postorder, s, m-1) and self.helper(postorder, m, e-1)

class Solution2:
    def verifyPostorder(self, postorder: [int]) -> bool:
        def recur(i, j):
            if i >= j: return True
            p = i
            while postorder[p] < postorder[j]: p += 1
            m = p
            while postorder[p] > postorder[j]: p += 1
            return p == j and recur(i, m - 1) and recur(m, j - 1)

        return recur(0, len(postorder) - 1)


if __name__ == '__main__':
    s = Solution().verifyPostorder
    # print(s([1,6,3,2,5]))
    # print(s([1,3,2,6,5]))
    print(s([1,2,5,10,6,9,4,3]))
