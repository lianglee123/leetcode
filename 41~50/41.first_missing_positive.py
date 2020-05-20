from typing import List


class Solution:
    """
    第一步
    """
    def firstMissingPositive(self, nums: List[int]) -> int:
        l = len(nums)
        for i in range(l):
            while nums[i] > 0 and  nums[i] <= l and nums[nums[i]-1] != nums[i]:
                # nums[i], nums[nums[i]-1] = nums[nums[i]-1], nums[i]  # 注意这种交换方法在是一个极大的BUG
                self.swap(nums, i, nums[i] - 1)
        for i, v in enumerate(nums):
            if v != i+1:
                return i+1
        return len(nums) + 1


    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]

if __name__ == '__main__':
    # s = Solution()
    # nums = [3, 4, -1, 1]
    # print("start: ", nums, flush=True)
    # print(s.step_1(nums))
    # print(nums, flush=True)
    nums = [-1, 4, 3, 1]
    i = 1
    nums[i], nums[nums[i]-1] = nums[nums[i]-1], nums[i]  # 这种交换方式的BUG
    print(nums)