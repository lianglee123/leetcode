
class Solution:
    """
    不是双指针，而是三指针
    """
    def sortColors(self, nums) -> None:
        """
        l 指针前的所有元素都是0(不包括l)
        r 指针后的所有元素都是2(不包括r)
        i 指针后到l指针所有的值必须保证不为0或2（包括l和i)
        不是
        """
        if len(nums) <= 1:
            return nums
        l, r = 0, len(nums) - 1
        i = l
        while l <= i <= r:
            # print("l, i, r: ", l, i, r)
            if nums[i] == 0:
                nums[l], nums[i] = nums[i], nums[l]
                l += 1
                i += 1
            elif nums[i] == 2:
                nums[r], nums[i] = nums[i], nums[r]
                r -= 1
            else:
                i += 1


if __name__ == '__main__':
    s = Solution().sortColors
    nums = [2, 0, 2, 1, 1,0]
    s(nums)
    print(nums)
    nums = [0, 0, 0, 0]
    s(nums)
    print(nums)
    nums = [1, 1, 1, 1]
    s(nums)
    print(nums)
    nums = [2, 2, 2, 2]
    s(nums)
    print(nums)
    nums = [0, 1]
    s(nums)
    print(nums)
    nums = [0, 2]
    s(nums)
    print(nums)
    nums = [0, 0]
    s(nums)
    print(nums)
    nums = [2, 2, 1]
    s(nums)
    print(nums)
