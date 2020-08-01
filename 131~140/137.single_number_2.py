from typing import *


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in range(32):
            sum = 0
            for n in nums:
                if ((n >> i & 1) == 1):
                    sum += 1
            sum %= 3
            res |= sum <<i
        return res