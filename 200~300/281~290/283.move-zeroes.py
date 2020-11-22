from typing import *


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        i = 0
        while i < len(nums):
            n = nums[i]
            if n == 0:
                i += 1
                continue
            j = i
            while j > 0 and nums[j-1] == 0:
                nums[j-1], nums[j] = nums[j], nums[j-1]
                j -= 1
            i += 1


if __name__ == '__main__':
    s = Solution().moveZeroes
    nums = [0, 0, 1, 0, 2,0, 0, 3, 4, 0]
    s(nums)
    print(nums)
    nums = [1, 0, 0, 0, 1]
    s(nums)
    print(nums)







