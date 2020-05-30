from typing import List


class Solution:
    """
    backTrack
    https://leetcode.com/problems/permutations/discuss/18247/My-elegant-recursive-C%2B%2B-solution-with-inline-explanation
    """
    def permuteUnique(self, nums: List[int]):
        res = []
        nums.sort()
        self.backTrack(nums, 0, res)
        return res


    def backTrack(self, nums, start, res):
        if start >= len(nums):
            res.append([i for i in nums])
            return
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[start]:
                continue
            nums[start], nums[i] = nums[i], nums[start]
            # 这种方法有问题的原因是，要一直保证res[start:]是排序的，但是，swap显然破坏了这个约束。
            self.backTrack(nums, start + 1, res)
            nums[start], nums[i] = nums[i], nums[start]


class Solution2:
    def permuteUnique(self, nums):
        res = []
        nums.sort()
        used = [False]*len(nums)
        self.backTrack(res, nums, [], used)
        return res

    def backTrack(self, res, nums, temp_list, used):
        if len(temp_list) == len(nums):
            res.append([i for i in temp_list])
            return
        for i, n in enumerate(nums):
            if used[i]:
                continue
            # 这里not used[i-1]的隐含意思很重要。在同一层级下(temp_list的长度为一个层级)，
            # 那些相同的值只被使用一次。
            if i > 0 and nums[i] == nums[i-1] and (not used[i-1]):  # not used[i-1]什么意思
                continue
            used[i] = True
            temp_list.append(n)
            self.backTrack(res, nums, temp_list, used)
            del temp_list[-1]
            used[i] = False


if __name__ == '__main__':
    s = Solution().permuteUnique
    nums = [1, 1, 2]
    res = s(nums)
    for i in res:
        print(i)