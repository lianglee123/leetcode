from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        s, e = 0, len(nums) - 1
        while s < e:
            mid = (s + e) // 2
            print("s: ", s, "e: ", e, "mid: ", mid)
            if target < nums[mid]:
                e = mid - 1
            elif target > nums[mid]:
                s = mid + 1
            else:
                return mid
        print("s: ", s, "e: ", e)
        return s

# e = mid:
# s:  0 e:  3 mid:  1
# s:  0 e:  1 mid:  0
# s:  1 e:  1
# 1
#
# e = mid - 1
#s:  0 e:  3 mid:  1
# s:  0 e:  0
# 0


if __name__ == '__main__':
    s = Solution().searchInsert
    # nums = [1, 3, 5, 6]
    # print(s(nums, 7))
    nums = [1, 3, 5, 6]
    print(s(nums, 2))