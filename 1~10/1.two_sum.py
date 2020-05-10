from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = {}
        for i, num in enumerate(nums):
            if num in a:
                return [a[num], i]
            else:
                a[target-num] = i

