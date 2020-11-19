from typing import List
"""
如果使用r=0， c=len(matrix[0]) - 1
如果m[r][c] > target, 那么该列可以排除在外
如果m[r][c] < target, 那么该行可以排除在外
这种搜索方法，是从右上交开始的。
"""

class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        r, c = 0, len(matrix[0])-1
        while r < len(matrix) and c >= 0:
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] < target:
                r += 1
            else:
                c -= 1
        return False

if __name__ == '__main__':
    s = Solution().findNumberIn2DArray
    m = [
        [1,   4,  7, 11, 15],
        [2,   5,  8, 12, 19],
        [3,   6,  9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]
    print(s(m, 5))
    print(s(m, 20))