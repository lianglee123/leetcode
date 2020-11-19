from typing import *


class Solution:
    def missionNumber(self, nums):
        n = len(nums)
        return n*(n+1)//2 - sum(nums)

class Solution2:
    def missionNumber(self, nums):
        res = 0
        for i, n in enumerate(nums):
            res ^= n
            res ^= i
        res ^= len(nums)
        return res
