from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
        dp = [0]*len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0:2])
        for i in range(2, len(nums)):
            dp[i] = max(nums[i]+dp[i-2], dp[i-1])
        return dp[-1]

class Solution2:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
        pre = nums[0]
        cur = max(nums[0:2])
        for i in range(2, len(nums)):
            cur, pre = max(nums[i]+pre, cur), cur
        return cur
