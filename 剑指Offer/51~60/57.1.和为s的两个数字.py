from typing import *


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums)-1
        while l < r:
            temp = nums[l] + nums[r]
            if temp == target:
                return [nums[l], nums[r]]
            elif temp > target:
                r -= 1
                while nums[r] == nums[r+1]:
                    r -= 1
            else:
                l += 1
                while nums[l] == nums[l-1]:
                    l += 1
        raise ValueError("not found")
