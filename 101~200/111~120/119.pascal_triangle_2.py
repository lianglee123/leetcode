from typing import *


def generate(self, numRows):
    """
    https://leetcode.com/problems/pascals-triangle/discuss/38128/Python-4-lines-short-solution-using-map.
    """
    res = [[1]]
    for i in range(1, numRows):
        res += [map(lambda x, y: x+y, res[-1] + [0], [0] + res[-1])]
    return res[:numRows]


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        while rowIndex:
            row =  list(map(lambda x, y: x+y, row + [0], [0] + row))
            rowIndex -= 1
        return row


if __name__ == '__main__':
    from pprint import pprint
    pprint(Solution().getRow(0))
    pprint(Solution().getRow(1))
    pprint(Solution().getRow(2))
    pprint(Solution().getRow(3))
    pprint(Solution().getRow(4))
    pprint(Solution().getRow(5))

