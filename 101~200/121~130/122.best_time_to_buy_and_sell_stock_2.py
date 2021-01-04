from typing import *
from utils import assert_eq

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        res = 0
        pre = prices[0]
        for p in prices:
            if p - pre > 0:
                res += (p - pre)
            pre = p
        return res


if __name__ == '__main__':
    s = Solution().maxProfit
    assert_eq(s([7, 1, 5, 3, 6, 4]), 7)
