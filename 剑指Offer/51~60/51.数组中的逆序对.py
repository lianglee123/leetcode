from typing import *




class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        self.cnt = 0
        self.mergeSort(nums, 0, len(nums)-1)
        return self.cnt

    def mergeSort(self, nums, start, end):
        if start >= end:
            return
        mid = (start + end) // 2
        self.mergeSort(nums, start, mid)
        self.mergeSort(nums, mid+1, end)
        self.mergeTowList(nums, start, mid, end)

    def mergeTowList(self, nums, start, mid, end):
        i, j = start, mid + 1
        temp = []
        while i <= mid and j <= end:
            if nums[i] <= nums[j]:
                temp.append(nums[i])
                i += 1
            else:
                temp.append(nums[j])
                j += 1
                self.cnt += (mid - i + 1)
        while i <= mid:
            temp.append(nums[i])
            i += 1

        while j <= end:
            temp.append(nums[j])
            j += 1
        for i in range(len(temp)):
            nums[start+i] = temp[i]

import bisect


class Solution2:
    def reversePairs(self, nums: List[int]) -> int:
        q = []
        res = 0
        for v in nums:
            v = -v
            i = bisect.bisect_left(q, v)
            res += i
            q.insert(i, v)
        return res

l1 = list(range(100))
l2 = list(range(100))


def a():
    l1.insert(50, 'A')


def b():
    l2[50:50] = 'B'


if __name__ == '__main__':
    # s = Solution2().reversePairs
    # print(s([7,5,6,4]))
    import timeit
    print(timeit.timeit("a()", "from __main__ import a", number=10000))
    print(timeit.timeit("b()", "from __main__ import b", number=10000))