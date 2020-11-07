from typing import *


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        while nums:
            rangeStr, i = self.findFirst(nums)
            res.append(rangeStr)
            nums = nums[i+1:]
        return res


    def findFirst(self, nums):
        if len(nums) == 1:
            return self.toRangeStr(nums[0], nums[0]), 0
        i = 0
        while i < len(nums):
            if i == 0:
                i += 1
                continue
            if nums[i] != nums[i-1] + 1:
                break
            i += 1
        return self.toRangeStr(nums[0], nums[i-1]), i-1

    def toRangeStr(self, start, end):
        if start == end:
            return str(start)
        else:
            return "%s->%s" % (start, end)


class Solution2:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        l = len(nums)
        res = []
        i = 0
        while i < l:
            j = i
            while j + 1 < l and nums[j+1] == nums[j] + 1:
                j += 1
            res.append(self.toRangeStr(nums[i], nums[j]))
            i = j + 1
        return res

    def toRangeStr(self, start, end):
        if start == end:
            return str(start)
        else:
            return "%s->%s" % (start, end)


if __name__ == '__main__':
    s = Solution().summaryRanges
    # print(s([0,1,2,4,5,7]))
    print(s([0,2,3,4,6,8,9]))



