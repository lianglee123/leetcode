from typing import *


class Solution:
    def searchMatrix(self, m, t):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not m or not m[0]:
            return False
        i, j = 0, len(m[0])-1
        while i < len(m) and j >= 0:
            v = m[i][j]
            if t == v:
                return True
            elif t < v:
                j -= 1
            elif t > v:
                i += 1
        return False




if __name__ == '__main__':
    s = Solution().searchMatrix
    m = [
        [1,   4,  7, 11, 15],
        [2,   5,  8, 12, 19],
        [3,   6,  9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]
    print(s(m, 9))
    print(s(m, 11))
    print(s(m, 12))
    print(s(m, 13))
    print(s(m, 12.5))