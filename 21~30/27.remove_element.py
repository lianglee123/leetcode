from typing import List


def assert_eq(val, expect):
    if val == expect:
        return
    else:
        err = "%s not equal %s" % (val, expect)
        raise AssertionError(err)


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        j = 0
        while j < len(nums):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
            j += 1
        return nums[:i]


if __name__ == '__main__':
    s = Solution().removeElement
    assert_eq(s([1, 2, 3, 4], 4), [1, 2, 3])
    assert_eq(s([3, 2, 2, 3], 3), [2, 2])
    print(s([3, 2, 2, 3], 3))