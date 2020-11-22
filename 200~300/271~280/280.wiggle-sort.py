from typing import *


class Solution:
    """
    https://www.cnblogs.com/grandyang/p/5177285.html
    """
    def wiggleSort(self, nums: List):
        nums.sort()
        for i in range(2, len(nums), 2):
            nums[i], nums[i-1] = nums[i-1], nums[i]


class Solution2:
    """
    https://www.cnblogs.com/grandyang/p/5177285.html
    """
    def wiggleSort(self, nums: List):
        if len(nums) <= 1:
            return
        for i in range(1, len(nums)):
            if i % 2 == 1:
                if nums[i] < nums[i-1]:
                    nums[i], nums[i-1] = nums[i-1], nums[i]
            else:
                if nums[i] > nums[i-1]:
                    nums[i], nums[i-1] = nums[i-1], nums[i]




