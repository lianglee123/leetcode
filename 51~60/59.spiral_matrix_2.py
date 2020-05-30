from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0]*n for i in range(n)]
        top = 0
        bottom = n - 1
        left = 0
        right = n - 1
        v = 1
        while True:
            for i in range(left, right+1):
                res[top][i] = v
                v += 1
            top += 1

            if left > right or top > bottom:
                break


            for i in range(top, bottom+1):
                res[i][right] = v
                v += 1
            right -= 1

            if left > right or top > bottom:
                break

            for i in range(right, left-1, -1):
                res[bottom][i] = v
                v += 1
            bottom -= 1

            if left > right or top > bottom:
                break

            for i in range(bottom, top-1, -1):
                res[i][left] = v
                v += 1
            left += 1
            if left > right or top > bottom:
                break
        return res


if __name__ == '__main__':
    s = Solution().generateMatrix
    for i in s(4):
        print(i)
