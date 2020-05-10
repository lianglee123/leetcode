from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        l = len(nums)
        res = set()  # 这种可以去重的方法是低效的，情况Solution2
        for i in range(l):
            j = i+1
            k = l-1
            target = - nums[i]
            while k > j:
                if nums[k]+nums[j] > target:
                    k -= 1
                elif nums[k]+nums[j] < target:
                    j += 1
                else:
                    res.add((nums[i], nums[j], nums[k]))
        return list(res)


class Solution2:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        length = len(nums)
        res = []  # 这种可以去重的方法是低效的，情况Solution2
        for i in range(length):
            l = i+1
            r = length-1
            target = - nums[i]
            while r > l:
                s = nums[r]+nums[l]
                if s > target:
                    r -= 1
                elif s < target:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    while r > l and nums[r] == nums[r-1]:
                        r -= 1
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    r -= 1
                    l += 1
        return res



if __name__ == '__main__':
    s = Solution2().threeSum
    print(s([-6, 2, 2, 2, 4, 4, 4]))