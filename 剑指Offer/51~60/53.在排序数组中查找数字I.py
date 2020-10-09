from typing import *


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.bisect_right(nums, target) - self.bisect_left(nums, target)

    def bisect_left(self, nums, target):
        l, r = 0, len(nums)
        while l < r:
            m = (r + l) // 2
            if nums[m] < target:
                l = m + 1
            else:
                r = m
        return l

    def bisect_right(self, nums, target):
        l, r = 0, len(nums)
        while l < r:
            m = (r + l) // 2
            if nums[m] > target:
                r = m
            else:
                l = m + 1
        return r




