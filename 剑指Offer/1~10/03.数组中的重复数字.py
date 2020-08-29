from typing import List


class Solution1:
    def findRepeatNumber(self, nums: List[int]) -> int:
        temp = [None] * len(nums)
        for i in range(0, len(nums)):
            n = nums[i]
            if temp[n] == n:   # 使用数组代替map
                return n
            temp[n] = n


class Solution2:
    def findRepeatNumber(self, nums: List[int]) -> int:
        for i, n in enumerate(nums):
            if n == i:
                continue
            while n != i:
                if nums[n] == n:
                    return n
                nums[i], nums[n] = nums[n], nums[i]



if __name__ == '__main__':
    s1 = Solution1().findRepeatNumber
    s2 = Solution2().findRepeatNumber
    print(s1([2, 3, 1, 0, 2, 5, 3]))
    print(s2([2, 3, 1, 0, 2, 5, 3]))

