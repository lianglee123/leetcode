from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        l = len(nums)
        res = set()
        for i in range(l):
            j = i+1
            k = l-1
            target = nums[i]
            while k > j:
                if nums[k]+nums[j] > target:
                    k -= 1
                elif nums[k]+nums[j] < target:
                    j += 1
                else:
                    res.add((nums[i], nums[j], nums[k]))
        return list(res)

