from typing import List


class Solution:
    """
    模仿26题，
    i指针之前的都是排过序的且保证唯二的值，j是处理迭代指针，
    j的目的是要找到那些唯二的值，跳过那些第三次重复的值
    和26题的不同在于，26题，每次交换i进一步就行了，但是这里不行，这里要看条件进一步或两步
    另外一个，可以把i和j看作指向不同的列表，这里指向相同的列表只是为了复用优化。

    啊啊，我用这种方法重视出现无法覆盖的corner情况。
    """
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)

        i = 0
        j = 1
        while j < len(nums):

            if nums[j] != nums[j-1] and j+1 < len(nums) and nums[j] != nums[j+1]: # one unique
                i += 1
                nums[i] = nums[j]
            elif nums[j] != nums[j-1] and j+1 >= len(nums):   # one unique
                i += 1
                nums[i] = nums[j]
            elif nums[j] == nums[j-1] and nums[j] != nums[j-2]:
                i += 1
                nums[i] = nums[j-1]
                if i+1 < len(nums):
                    i += 1
                    nums[i] = nums[j]

                # print(i, j, nums)
                # nums[i], nums[i-1] = nums[j], nums[j-1]
            j += 1
        return i + 1

class Solution2:
    """
    这种方法，明显优越的多，而且可以解决Kduplidate的问题
    这种方法，遍历所有值, 只要满足i的条件，就把n加入i的数组即可。

    solution1 和 solution2的思路是相反的:
    solution1我想在遍历j的时候，取出合法值，然后不加验证的加入i
    solution2遍历j,取出所有值，加入i的时候判断是否合法。很明显，在这个问题上solution2更简洁高超一点。
    双向思维。
    """
    def removeDuplicates(self, nums):
        i = 0
        for n in nums:
            if i < 2 or n > nums[i-2]:
                nums[i] = n
                i += 1
        return i


if __name__ == '__main__':
    s = Solution().removeDuplicates
    nums = [1, 1, 1, 2, 2, 3]
    print(s(nums), nums)

    nums = [1, 2, 2]
    print(s(nums), nums)

    nums = [1,2,2,2]
    print(s(nums), nums)

    nums = [1,2,2,2,2]
    print(s(nums), nums)

    nums = [1,1,1,1,1]
    print(s(nums), nums)

