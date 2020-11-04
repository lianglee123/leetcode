from typing import *

"""
最容易理解和简单的方式是使用堆
精巧的方法是使用快排相同的思路
"""

import heapq


class Solution:

    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = nums[:k]
        heapq.heapify(h)
        for i in range(k, len(nums)):
            if nums[i] > h[0]:
                heapq.heappop(h)
                heapq.heappush(h, nums[i])
        return h[0]
