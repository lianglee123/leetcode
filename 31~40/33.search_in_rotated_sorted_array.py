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


if __name__ == '__main__':
    s = Solution().search
    # print(s([4, 5, 6, 7, 0, 1, 2], 0))
    print(s([1, 3], 3))