from typing import *


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        result = [[1]]
        for rowIndex in range(1, numRows):
            row = []
            for i in range(rowIndex+1):
                row.append(self.getPreLeft(result[-1], i) + self.getPreRight(result[-1], i))
            result.append(row)
        return result

    def getPreLeft(self, preRow, index):
        preLeftIndex = index - 1
        if preLeftIndex < 0:
            return 0
        else:
            return preRow[preLeftIndex]

    def getPreRight(self, preRow, index):
        preRightIndex = index
        if preRightIndex > len(preRow)-1 :
            return 0
        else:
            return preRow[preRightIndex]


def generate(self, numRows):
    """
    https://leetcode.com/problems/pascals-triangle/discuss/38128/Python-4-lines-short-solution-using-map.
    """
    res = [[1]]
    for i in range(1, numRows):
        res += [map(lambda x, y: x+y, res[-1] + [0], [0] + res[-1])]
    return res[:numRows]

if __name__ == '__main__':
    from pprint import pprint
    pprint(Solution().generate(0))
    pprint(Solution().generate(1))
    pprint(Solution().generate(2))
    pprint(Solution().generate(3))
    pprint(Solution().generate(4))
    pprint(Solution().generate(10))