from typing import *


class Solution:
    """
    方案一：使用或与
    注意，与或的方案不适用于此题，因为输入游客可能为：[1, 2, 2, 2, 2]
    """
    def findDuplicate(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            res ^= n
        for i in range(1, len(nums)):
            res ^= i
        return res


class Solution2:
    """
    可以把这个问题看成求链表的环的起始点的问题
    快慢双指针法
    """
    def findDuplicate(self, nums: List[int]):
        if not nums:
            return -1
        slow = nums[0]
        fast = nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        fast = 0
        while fast != slow:
            fast = nums[fast]
            slow = nums[slow]
        return slow


class Solution3:
    """
    使用二分法
    https://leetcode.com/problems/find-the-duplicate-number/discuss/72844/Two-Solutions-(with-explanation)%3A-O(nlog(n))-and-O(n)-time-O(1)-space-without-changing-the-input-array
    """
    def findDuplicate(self, nums: List[int]):
        if not nums:
            return -1
        low, high = len(nums) - 1
        while low < high:
            mid = low + (high - low) // 2
            count = 0
            for n in nums:
                if n <= mid:
                    count += 1
            if count <= mid:
                low = mid + 1
            else:
                high = mid
        return low



if __name__ == '__main__':
    s = Solution().findDuplicate
    print(s([1, 3, 4, 2, 2]))





