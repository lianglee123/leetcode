from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0
        for i, n in enumerate(nums):
            if max_reach < i:
                return False
            max_reach = max(i+n, max_reach)
            if max_reach >= len(nums) - 1:
                return True
        return True


class SolutionDP:
    """
    https://leetcode.com/problems/jump-game/discuss/20923/Java-Solution-easy-to-understand
    dp[i]的含义是：从i能不能跳到末尾, 假设i能跳到的最大位置是i+j, 那么， dp[i] = any(dp[i+1~i+j])
    """
    def canJump(self, nums):
        l = len(nums)
        print(nums)
        dp = [False] * l  #
        dp[-1] = True
        for i in range(l-2, -1, -1):
            j = nums[i]
            print(i, j)
            dp[i] = any(dp[i:i+j+1])
            print(dp)
        return dp[0]



if __name__ == '__main__':
    s = SolutionDP().canJump
    ns = [2, 3, 1, 1, 4]
    s(ns)