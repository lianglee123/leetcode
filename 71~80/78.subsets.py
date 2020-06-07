from  typing import List


class Solution:
    """
    backTrace
    """
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.backTrace(res, nums, 0, len(nums)-1, [])
        res.sort(key=lambda x: len(x))
        return res

    def backTrace(self, res, nums, start, end, temp):
        res.append([v for v in temp])
        if len(nums) == len(temp):
            return
        for i in range(start, end+1):
            temp.append(nums[i])
            self.backTrace(res, nums, i+1, end, temp)
            temp.pop()


def p_m(m):
    if not m:
        return
    print("*"*10)
    for row in m:
        print(row)


if __name__ == '__main__':
    s = Solution().subsets
    nums = [1, 2, 3]
    p_m(s(nums))
