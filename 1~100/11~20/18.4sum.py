from typing import List


class Solution:
    def fourSum(self, nums, target):
        nums.partition_sort()
        results = []
        self.findNSum(nums, target, 4, [], results)
        return results

    def findNSum(self, nums, target, N, result: List[int], results: List[List[int]]):
        if len(nums) < N or N < 2:
            return
        if N == 2:
            l, r = 0, len(nums)-1
            while l < r:
                s = nums[l] + nums[r]
                if s == target:
                    results.append(result+[nums[l], nums[r]])
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while r > l and nums[r] == nums[r+1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif s < target:
                    l += 1
                else:
                    r -= 1
        else:
            for i in range(0, len(nums)-N+1):
                if target<nums[i]*N or target>nums[-1]*N:
                    break
                if i == 0 or i > 0 and nums[i-1] != nums[i]:
                    self.findNSum(nums[i+1:], target-nums[i], N-1, result+[nums[i]], results)


if __name__ == '__main__':
    s = Solution().findNSum
    a = [-6, 2, 2, 2, 4, 4, 4]
    res = []
    s(a, 0,4, [], res)
    print(res)

