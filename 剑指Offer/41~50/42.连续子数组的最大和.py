from typing import *



class WrongSolution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            raise ValueError("nums is empty")
        curMax = res = nums[0]
        for n in nums[1:]:
            newMax = curMax + n
            if newMax >= curMax:
                curMax = newMax
            else:
                curMax = n
            res = max(res, curMax)
        return res


class Solution:
    """
    dp[i]: 以i结尾的maxSubArray
    dp[i] = max(dp[i-1]+nums[i], nums[i])
    """
    def maxSubArray(self, nums: List[int]) -> int:
        cur_max = nums[0]
        res = cur_max
        for i in range(1, len(nums)):
            cur_max = max(cur_max+nums[i], nums[i])
            res = max(res, cur_max)
        return res




if __name__ == '__main__':
    s = Solution().maxSubArray
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(s(nums))


