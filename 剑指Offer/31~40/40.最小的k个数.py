from typing import *
import random


class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        return sorted(arr)[:k]


import heapq


class Solution3:
    """
    要注意：python的heap是小根堆，所以这里要反转。
    求最大k个数要用小根堆，求最小k个数要用大根堆，这是为什么呢？
    """
    def getLeastNumbers(self, arr: List[int], k: int):
        if k == 0:
            return list()
        hp = [-x for x in arr[:k]]
        heapq.heapify(hp)
        for i in range(k, len(arr)):
            if -arr[i] > hp[0]:
                heapq.heappop(hp)
                heapq.heappush(hp, -arr[i])
        return [-x for x in hp]


class Solution2:
    def partition(self, nums, l, r):
        pivot = nums[r]
        i = l - 1
        for j in range(l, r):
            if nums[j] <= pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1], nums[r] = nums[r], nums[i + 1]
        return i + 1

    def randomized_partition(self, nums, l, r):
        i = random.randint(l, r)
        nums[r], nums[i] = nums[i], nums[r]
        return self.partition(nums, l, r)

    def partition_sort(self, arr, l, r, k):
        pos = self.randomized_partition(arr, l, r)
        num = pos - l + 1
        if k < num:
            self.partition_sort(arr, l, pos - 1, k)
        elif k > num:
            self.partition_sort(arr, pos + 1, r, k - num)

    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if k == 0:
            return list()
        self.partition_sort(arr, 0, len(arr) - 1, k)
        return arr[:k]


class Solution4:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if k == 0:
            return []
        self.partition_sort(arr, 0, len(arr)-1, k)
        return arr[:k]

    def partition_sort(self, arr, l, r, k):
        if l >= r:
            return
        pos = self.partition1(arr, l, k)
        num = pos - l + 1
        if num > k:
            self.partition_sort(arr, l, pos-1, k)
        elif num < k:
            self.partition_sort(arr, pos+1, r, k - num)

    def partition1(self, arr, l, r):
        """
        i + 1的位置是分界点，此处应该放置pivot
        (i, j]上的数据必须大于pivot
        [L, i]上的数据必须小于pivot
        """
        pivot = arr[r]
        i = l - 1
        for j in range(l, r):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i+1], arr[r] = arr[r], arr[i+1]
        return i + 1


if __name__ == '__main__':
    arrs1 = list(range(10))
    random.shuffle(arrs1)
    s = Solution2().getLeastNumbers
    print(s(arrs1, 5))
    assert sorted(s(arrs1, 5)) == list(range(5))


