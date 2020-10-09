from typing import *


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l, r = 0, len(nums)
        while r > l:
            m = (r + l) // 2
            if nums[m] == m:
                l = m + 1
            else:
                r = m
        return l

if __name__ == '__main__':
    s = Solution().missingNumber
    assert s([0, 1, 3]) == 2
    assert s([0,1,2,3,4,5,6,7,9]) == 8


