from typing import *



class Solution:
    def rob(self, nums):
        if not nums:
            return 0
        if nums <= 2:
            return max(nums)
        max1 = self.robLine(nums[:-1])
        max2 = self.robLine(nums[1:])
        return max(max1, max2)


    def robLine(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
        pre = nums[0]
        cur = max(nums[0:2])
        for i in range(2, len(nums)):
            cur, pre = max(nums[i]+pre, cur), cur
        return cur
