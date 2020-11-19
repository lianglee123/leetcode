from typing import List
"""
这个题要求的是找出任意一个重复的数字，而不是所有重复的数字
Solution1和Solution2一脉相承，只不过S1额外新建了一个数字
S1的思路：
新建一个数组temp, 把已经出现的数字，放在他应该出现的位置上，
如果一个数字是第二次出现，返回该数字即可
S2和S1的思路一脉相承，只不过S2复用了参数数组。但是S2更难理解一些
S2的nums[n] == n

---
如果要返回所有重复的，使用排序算法就更通用一点。
但是S1和S2的方法还可以使用。只不过需要去重
"""

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
                if nums[n] == n:   # 数值n应该放在第n个位置，但是
                    return n
                nums[i], nums[n] = nums[n], nums[i]


"""
变种：返回所有重复的
"""
class C1Solution1:
    def findRepeatNumbers(self, nums: List[int]) -> List[int]:
        temp = [None] * len(nums)
        res = []
        for i in range(0, len(nums)):
            n = nums[i]
            if temp[n] == n:   # 使用数组代替map
                res.append(n)
                continue
            temp[n] = n
        return res


class C2Solution2:
    def findRepeatNumbers(self, nums: List[int]) -> int:
        for i, n in enumerate(nums):
            if n == i:
                continue
            while n != i:
                if nums[n] == n:   # 数值n应该放在第n个位置，但是
                    return n
                nums[i], nums[n] = nums[n], nums[i]


if __name__ == '__main__':
    s1 = Solution1().findRepeatNumber
    s2 = Solution2().findRepeatNumber
    assert s1([2, 3, 1, 0, 2, 5, 3]) == 2
    assert s2([2, 3, 1, 0, 2, 5, 3]) == 2

    c1s1 = C1Solution1().findRepeatNumbers
    print(c1s1([2, 3, 1, 0, 2, 5, 3]))


