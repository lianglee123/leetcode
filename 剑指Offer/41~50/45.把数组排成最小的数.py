from typing import *
from functools import cmp_to_key


class Solution:
    def minNumber(self, nums: List[int]) -> str:
        numsStr = [str(n) for n in nums]
        def cmp(x, y):
            a, b = x + y, y + x
            if a > b: return 1
            elif a < b: return -1
            else: return 0

        numsStr.sort(key=cmp_to_key(cmp))
        return "".join(numsStr).lstrip("0")


class Solution2:
    def minNumber(self, nums: List[int]) -> str:
        # 如此优雅的快排
        def fast_sort(l , r):
            if l >= r: return
            i, j = l, r
            while i < j:
                while strs[j] + strs[l] >= strs[l] + strs[j] and i < j: j -= 1
                while strs[i] + strs[l] <= strs[l] + strs[i] and i < j: i += 1
                strs[i], strs[j] = strs[j], strs[i]
            strs[i], strs[l] = strs[l], strs[i]
            fast_sort(l, i - 1)
            fast_sort(i + 1, r)

        strs = [str(num) for num in nums]
        fast_sort(0, len(strs) - 1)
        return ''.join(strs)


def fast_sort(nums, l, r):
    if l >= r:
        return
    i, j = l, r
    while i < j:
        while nums[j] >= nums[l] and i < j: j -= 1
        while nums[i] <= nums[l] and i < j: i += 1
        nums[i], nums[j] = nums[j], nums[i]


if __name__ == '__main__':
    s = Solution().minNumber
    print(s([10, 2]))