from typing import *


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        i = 0
        j = 0
        sum = 0
        minLen = float('inf')
        while j < len(nums):
            sum += nums[j]
            while sum >= s:
                minLen = min(minLen, j-i+1)
                sum -= nums[i]
                i += 1
                print('i, j', i, j)
            j += 1
        return 0 if minLen == float('inf') else minLen


if __name__ == '__main__':
    s = Solution().minSubArrayLen
    print(s(7, [2, 3, 1, 2, 4, 3]))