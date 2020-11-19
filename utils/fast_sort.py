from typing import *


class Solution2:
    def quick_sort(self, nums: List[int]) -> str:
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


class Solution1:
    def quick_sort(self, array):
        self._quick_sort(array, 0, len(array)-1)

    def _quick_sort(self, array, l, r):
        if l < r:
            q = self.partition(array, l, r)
            self._quick_sort(array, l, q - 1)
            self._quick_sort(array, q + 1, r)

    def partition(self, array, l, r):
        """
        迭代处理左右的数组时，都要排除掉pivot, 防止死循环
        partition:
            (, i]所有的数都小于等于pivot
            (i, j]所有数都大于pivot
            pivot作为分界线单独处理
        """
        x = array[r]
        i = l - 1
        for j in range(l, r):
            if array[j] <= x:
                i += 1
                array[i], array[j] = array[j], array[i]
        array[i + 1], array[r] = array[r], array[i+1] # array[R]是pivot, 要确保pivot在分界线上，才能防止循环递归
        return i + 1


class Solution3:

    def quick_sort(self, array):
        self._quick_sort(array, 0, len(array)-1)

    def _quick_sort(self, nums, l, r):
        """
        nums[l]是pivot
        (j R],
        [L, i) 所有数字都小于等于pivot
        在i与j相遇的地方停止：
            - 其值一定是小于等于pivot的? 如何证明
            最后的停止条件是i==j:
                j停止的地方 < pivot
                i停止的地方 > pivot，但是紧接着有一次i,j的交换，所以导致，i停止的地方，也是 < pivot
            所以nums[i]一定<pivot, 因此可以交换i和pivot
        """
        if l >= r:
            return
        i, j = l, r
        while i < j:
            while nums[j] >= nums[l] and i < j: j -= 1
            while nums[i] <= nums[l] and i < j: i += 1
            nums[i], nums[j] = nums[j], nums[i]
        nums[i], nums[l] = nums[l], nums[i]

        self._quick_sort(nums, l, i - 1)
        self._quick_sort(nums, i + 1, r)



if __name__ == '__main__':
    import random

    nums = list(range(10))
    random.shuffle(nums)
    print(nums)
    print(Solution3().quick_sort(nums))
    print(nums)
