from typing import List

def assert_eq(val, expect):
    if val == expect:
        return
    else:
        err = "%s not equal %s" % (val, expect)
        raise AssertionError(err)


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        i = 0
        j = 1
        while j < len(nums):
            if nums[j] != nums[j-1]:
                i += 1
                nums[i] = nums[j]
            j += 1
        return i+1



if __name__ == '__main__':
    s = Solution().removeDuplicates
    nums = [1, 1, 2, 2, 3, 3]
    res = [1, 2, 3]
    assert_eq(nums[:s(nums)], res)

    nums = [1, 2, 2, 3, 3]
    assert_eq(nums[:s(nums)], res)

    nums = [1, 2, 2, 3, 3]
    assert_eq(nums[:s(nums)], res)

    nums = [1, 1, 1, 1]
    assert_eq(nums[:s(nums)], [1])

    nums = [1]
    assert_eq(nums[:s(nums)], [1])
    nums = [1]
    assert_eq(s(nums), 1)

    nums = []
    assert_eq(s(nums), 0)
