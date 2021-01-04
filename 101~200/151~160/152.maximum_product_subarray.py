from typing import *


class Solution:
    """
    这种做法我不知道原理了
    """
    def maxProduct(self, nums: List[int]) -> int:
        prefix, suffix, max_so_far = 0, 0, float('-inf')
        for i in range(len(nums)):
            prefix = (prefix or 1) * nums[i]
            suffix = (suffix or 1) * nums[~i]
            max_so_far = max(max_so_far, prefix, suffix)
        return max_so_far


class Solution2:
    def maxProduct(self, nums: List[int]) -> int:
        imax = imin = ans = nums[0]
        for n in nums[1:]:
            if n < 0:
                imax, imin = imin, imax  # 如果n<0, 那么最大最小就要交换
            imax = max(n, imax * n)
            imin = min(n, imin * n)
            ans = max(ans, imax)
        return ans


class Solution3:
    def maxProduct(self, nums: List[int]):
        imax = imin = ans = nums[0]
        for n in nums[1:]:
            temp1 = imax * n
            temp2 = imin * n
            imax = max(n, temp1, temp2)
            imin = min(n, temp1, temp2)
            ans = max(ans, imax)
        return ans


if __name__ == '__main__':
    s = Solution().maxProduct
    print(s([2,3,-2,4]))
    print(s([-2,0,-1]))
