from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        low, hi = 0, len(nums) - 1
        res = [-1, -1]

        while low < hi:
            mid = (low + hi) // 2
            if target > nums[mid]:
                low = mid + 1
            else:
                hi = mid  # 因为是找上下边界，所以当等于的情况，hi依然向下移动
        if target == nums[low]:
            res[0] = low
        else:
            return [-1, -1]
        print("low: ", low)
        hi = len(nums) - 1
        while low < hi:
            mid = (low + hi) // 2 + 1  ## 要注意这里，不加1会造成死循环
            print("hi: ", hi)
            print("low: ", low)
            print("mid: ", mid)
            if target < nums[mid]:
                hi = mid - 1
            else:
                low = mid # 因为是找上下边界，所以当等于的情况，low依然向上移动
        res[1] = low
        return res


if __name__ == '__main__':
    s = Solution().searchRange
    print(s([5,7,7,8,8,10], 8))
