from typing import *



class Solution:
    """
    dp
    """
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums: return 0
        dp = [1] * len(nums)
        res = 1
        for i, n in enumerate(nums):
            if i == 0: continue
            for j in range(0, i):
                if n > nums[j]:
                    dp[i] = max(dp[i], dp[j])
            res = max(res, dp[i])
        return res



class Solution2:
    """
    巧思
    https://leetcode-cn.com/problems/longest-increasing-subsequence/solution/zui-chang-shang-sheng-zi-xu-lie-dong-tai-gui-hua-e/
    查看coldMe的回答
    """
    def lengthOfLIS(self, nums):
        size = len(nums)
        if size < 2:
            return size
        cell = [nums[0]]
        for num in nums[1:]:
            if num > cell[-1]:
                cell.append(num)
                continue
            l, r = 0, len(cell)-1
            while l < r:
                mid = l + (r - l)//2
                if cell[mid]<num:
                    l = mid + 1
                else:
                    r = mid
            cell[l] = num
        return len(cell)


    def findMinLargerThanMe(self, nums, target):
        """
        [L, R]之间的，可能是我们要找的值。
        当通过nums[m] < target, 就可以排除[L, M]之间的值了
        所以L, R要更新为[M+1, R]
        如果nums[m] >= target, 说明可能值在[L,M]之间，所以要更新为[L, M]
        注意，如果不存在目标值，返回值为len(nums)
        :param nums:
        :param target:
        :return:
        """
        l, r, = 0, len(target) - 1
        while l < r:
            m = l + (r - l)//2
            if nums[m] < target:
                l = m + 1
            else:
                r = m
        return l
