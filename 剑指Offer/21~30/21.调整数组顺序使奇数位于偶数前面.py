from typing import *


class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums)-1
        while l < r:
            if nums[l] % 2 == 0:
                nums[l], nums[r] = nums[r], nums[l]
                r -= 1
            else:
                l += 1
        return nums

class Solution2:
    def exchange(self, nums: List[int]) -> List[int]:
        nums.sort(key=lambda x: x%2 == 0)
        return nums

if __name__ == '__main__':
    s = Solution2().exchange
    print(s([2, 1]))
    print(s([1, 2]))
    print(s([1, 1]))
    print(s([2, 2]))
    print(s([2]))
    print(s([1]))
    print(s([2,1,2,2, 1, 2, 3, 1]))
