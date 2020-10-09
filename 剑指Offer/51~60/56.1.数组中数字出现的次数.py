from typing import *

import functools


class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        ret = functools.reduce(lambda x, y: x^y, nums)
        if ret == 0:
            raise ValueError("nums error")
        temp = 1
        while (ret & temp) == 0:
            temp = temp << 1
        a, b = 0, 0
        for n in nums:
            if temp & n:
                a ^= n
            else:
                b ^= n
        return [a, b]






if __name__ == '__main__':
    s = Solution().singleNumbers


