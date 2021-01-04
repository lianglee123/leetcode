from typing import *


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        for i, v in enumerate(nums):
            l = nums[i-1] if i > 0 else float('-inf')
            r = nums[i+1] if i < len(nums)-1 else float('-inf')
            if  l < v and r < v:
                return i
        return -1


if __name__ == '__main__':
    s = Solution().findPeakElement
    print(s([1, 2, 3, 1]))
    print(s([1,2,1,3,5,6,4]))

