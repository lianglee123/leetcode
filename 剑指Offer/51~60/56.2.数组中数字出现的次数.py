from typing import *


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for i in range(32):
            cnt = 0
            for n in nums:
                if n & (1 << i):
                    cnt += 1
            if (cnt % 3 == 1):
                ans ^= (1<<i)
        return ans




