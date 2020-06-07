from typing import List

def assert_eq(val, expect):
    if val == expect:
        return
    else:
        err = "%s not equal %s" % (val, expect)
        raise AssertionError(err)


class Solution:
    """
    Round2: i左边是排好序且无重复的的(包括i)，j是迭代处理指针。
    把j碰到的第一个唯一数，放到i的位置。
    参考80, 这种方法其实并不高明。
    """
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        i = 0
        j = 1
        while j < len(nums):
            if nums[j] != nums[j-1]:
                print("start swap: ", nums, i, j)
                i += 1
                nums[i] = nums[j]   # 注意，这里不是swap，而是直接覆盖了，这是非常重要的一点
                print("end swap: ", nums, i, j)
            j += 1
        return i+1


class Solution2:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        i = 0
        for n in nums:
            if n != nums[i]:
                i += 1
                nums[i] = n
        return i + 1


if __name__ == '__main__':
    s = Solution2().removeDuplicates
    nums = [1, 1, 2, 2, 3]
    print(s(nums))
    # nums = [1, 1, 2, 2, 3, 3]
    # res = [1, 2, 3]
    # assert_eq(nums[:s(nums)], res)
    #
    # nums = [1, 2, 2, 3, 3]
    # assert_eq(nums[:s(nums)], res)
    #
    # nums = [1, 2, 2, 3, 3]
    # assert_eq(nums[:s(nums)], res)
    #
    # nums = [1, 1, 1, 1]
    # assert_eq(nums[:s(nums)], [1])
    #
    # nums = [1]
    # assert_eq(nums[:s(nums)], [1])
    # nums = [1]
    # assert_eq(s(nums), 1)
    #
    # nums = []
    # assert_eq(s(nums), 0)
