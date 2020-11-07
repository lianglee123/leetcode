from typing import *


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        if not nums:
            return res
        cand1, count1 = nums[0], 0
        cand2, count2 = nums[0], 0
        for n in nums:
            if cand1 == n:
                count1 += 1
                continue
            if cand2 == n:
                count2 += 1
                continue
            if count1 == 0:
                cand1 = n
                count1 += 1
                continue
            if count2 == 0:
                cand2 = n
                count2 += 1
                continue
            count1 -= 1
            count2 -= 1

        count1 = 0
        count2 = 0
        for n in nums:
            if n == cand1: count1 += 1
            elif n == cand2: count2 += 1
        if count1 > len(nums)/3 > 0: res.append(cand1)
        if count2 > len(nums)/3 > 0: res.append(cand2)
        return res
