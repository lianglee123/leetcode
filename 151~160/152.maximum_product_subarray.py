from typing import *


class Solution:
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
            if n < 0: imax, imin = imin, imax
            imax = max(n, imax * n)
            imin = min(n, imin * n)
            ans = max(ans, imax)
        return ans

if __name__ == '__main__':
    s = Solution().maxProduct
    print(s([2,3,-2,4]))
    print(s([-2,0,-1]))