from typing import *



class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        for i in range(len(nums)):
            for j in range(i+1, i+1+k):
                if j >= len(nums):
                    break
                if abs(nums[i]-nums[j]) <= t:
                    return True
        return False


from sortedcontainers import SortedSet


class Solution2:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        sorted_set = SortedSet()

        for i in range(len(nums)):
            num = nums[i]

            # find the successor of current element
            if sorted_set and sorted_set.bisect_left(num) < len(sorted_set):  # 存在刚好比num大的数
                if sorted_set[sorted_set.bisect_left(num)] <= num + t:
                    return True

            # find the predecessor of current element
            if sorted_set and sorted_set.bisect_left(num) != 0:  # 存在刚好比num小的数
                if num <= sorted_set[sorted_set.bisect_left(num) - 1] + t:
                    return True

            sorted_set.add(num)
            if len(sorted_set) > k:
                sorted_set.remove(nums[i - k])

        return False

