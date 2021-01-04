from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = matrix
        res = []
        if not m or (not m[0]):
            return res
        top = 0
        bottom = len(m) - 1
        left = 0
        right = len(m[0]) - 1

        while True:
            for i in range(left, right+1):
                res.append(m[top][i])
            top += 1

            if left > right or top > bottom:
                break

            for i in range(top, bottom+1):
                res.append(m[i][right])
            right -= 1

            if left > right or top > bottom:
                break

            for i in range(right, left-1, -1):
                res.append(m[bottom][i])
            bottom -= 1

            if left > right or top > bottom:
                break

            for i in range(bottom, top-1, -1):
                res.append(m[i][left])
            left += 1

            if left > right or top > bottom:
                break

        return res


if __name__ == '__main__':
    s = Solution().spiralOrder
    m = [['a', 'b', 'c'],
         ['d', 'e', 'f'],
         ['g', 'h', 'i']
         ]
    print(s(m))

