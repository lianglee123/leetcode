from typing import List


def assert_eq(val, expect):
    if val == expect:
        return
    else:
        err = "%s not equal %s" % (val, expect)
        raise AssertionError(err)


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums or len(nums) == 1:
            return
        x = len(nums) - 2
        while x >= 0:
            if nums[x] < nums[x+1]:
                break
            x -= 1
        if x == -1:
            self.reverse(nums, 0, len(nums)-1)
            return

        y = len(nums) - 1
        while y > x:
            if nums[y] > nums[x]:
                break
            y -= 1
        nums[x], nums[y] = nums[y], nums[x]
        self.reverse(nums, x+1, len(nums) - 1)




    def reverse(self, nums: List, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1



if __name__ == '__main__':
    # r = Solution().reverse
    # nums = [1, 2, 3, 4]
    # r(nums, 0, 3)
    # assert_eq(nums, [4, 3, 2, 1])
    # r(nums, 0, 3)
    # assert_eq(nums, [1, 2, 3, 4])

    r = Solution().nextPermutation

    nums = [1, 2]
    r(nums)
    assert_eq(nums, [2, 1])

    nums = [1, 3, 2]
    r(nums)
    assert_eq(nums, [2, 1, 3])

    nums = [5, 1, 1]
    r(nums)
    assert_eq(nums, [1, 1, 5])