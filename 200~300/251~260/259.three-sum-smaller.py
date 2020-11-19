from typing import *


class Solution:
    """
    暴力
    """
    def threeSumSmaller(self, nums, target):
        if len(nums) < 0:
            return 0
        res = 0
        nums.sort()
        for i in range(len(nums)-2):
            left = i + 1
            t1 = target - nums[i]
            for j in range(left, len(nums)):
                t2 = t1 - nums[j]
                for k in range(j+1, len(nums)):
                    if nums[k] < t2:
                        res += 1
        return res


class Solution1:
    """
    双指针
    """
    def threeSumSmaller(self, nums, target):
        if len(nums) < 3:
            return 0
        res = 0
        n = len(nums)
        nums.sort()
        for i in range(0, n-2):
            l = i + 1
            r = n - 1
            while l < r:
                if nums[i] + nums[l] + nums[r] < target:
                    res += (r - l)  # eg [-2,0,1,3] 4,so -2,0,3满足，-2,0,1也满足
                    l += 1
                else:
                    r -= 1


