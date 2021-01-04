from typing import List


class Solution:
    """
    不是3Sum的翻版。
    这个问题要考虑的问题是：要如何及时的停止
    """
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        l = len(nums)
        closest = float('inf')
        res = 0
        for i in range(l):
            j = i+1
            k = l-1
            while k > j:
                sum = nums[k] + nums[j] + nums[i]
                diff = sum - target
                if abs(diff) < abs(closest):
                    closest = diff
                    res = sum
                if diff == 0:
                    return res
                elif diff > 0:
                    k -= 1
                else:
                    j += 1
        return res
