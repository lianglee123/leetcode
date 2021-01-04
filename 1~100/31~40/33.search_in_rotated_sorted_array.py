from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        minIndex = self.findMinIndex(nums)
        l = len(nums)
        if target <= nums[-1]:
            s = minIndex
            e = l - 1
        else:
            s = 0
            e = minIndex - 1

        while s <= e:
            mid = (s + e) // 2
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                s = mid + 1
            else:
                e = mid - 1
        return -1

    def findMinIndex(self, nums):
        s, e = 0, len(nums)-1
        while s < e:
            mid = (s + e) // 2
            if nums[mid] > nums[e]:
                s = mid + 1  # 这里不加1会陷入死循环
            else:
                e = mid
        return s


class Side:
    LEFT = "LEFT"
    RIGHT = "RIGHT"


class Solution2:
    def search(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums)
        MAX_VALUE = float('inf')
        MIN_VALUE = float('-inf')
        while lo < hi:
            mid = lo + (hi - lo) // 2
            mid_side = self.get_side(nums, nums[mid])
            target_side = self.get_side(nums, target)
            if mid_side == target_side:
                num = nums[mid]
            else:
                if target_side == Side.RIGHT:
                    num = MAX_VALUE  # 控制指针的行进方向
                else:
                    num = MIN_VALUE
            if num < target:
                lo = mid + 1
            elif num > target:
                hi = mid
            else:
                return mid
        return -1



    def get_side(self, nums, value):
        if value < nums[0]:
            return Side.RIGHT
        else:
            return Side.LEFT


class Solution3:
    def search(self, nums, target):
        l, r = 0, len(nums)-1
        while l <= r:
            mid = l + (r-l)//2
            if nums[mid] == target:
                return mid
            while l < mid and nums[l] == nums[mid]: # tricky part
                l += 1
            # the first half is ordered
            if nums[l] <= nums[mid]:
                # target is in the first half
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            # the second half is ordered
            else:
                # target is in the second half
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1



if __name__ == '__main__':
    s = Solution().search
    # print(s([4, 5, 6, 7, 0, 1, 2], 0))
    print(s([1, 3], 3))