from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = {}
        for i, num in enumerate(nums):
            if num in a:
                return [a[num], i]
            else:
                a[target-num] = i


class Solution2:
    """
    这个方法，只能找到目标数，无法找到目标数的索引
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        i, j = 0, len(nums) - 1
        while i < j:
            s = nums[i] + nums[j]
            if nums[i] + nums[j] == target:
                return [i, j]
            elif s < target:
                i += 1
            else:
                j -= 1


if __name__ == '__main__':
    s = Solution2().twoSum
    print(s([2, 3, 4], 6))