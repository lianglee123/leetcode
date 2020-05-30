from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_max = nums[0]
        res = cur_max
        for i in range(1, len(nums)):
            cur_max = max(cur_max+nums[i], nums[i])
            res = max(res, cur_max)
        return res


if __name__ == '__main__':
    s = Solution()
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(s.maxSubArray(nums))
