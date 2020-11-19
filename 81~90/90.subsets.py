from typing import List


class Solution:
    """
    backTrace
    """
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        self.backTrace(res, nums, 0, len(nums)-1, [])
        res.sort(key=lambda x: len(x))
        return res

    def backTrace(self, res, nums, start, end, temp):
        res.append([v for v in temp])
        if len(nums) == len(temp):
            return
        i = start
        while i <= end:
            if i >= start and nums[i] == nums[i-1]:
                i += 1
                continue
            temp.append(nums[i])
            self.backTrace(res, nums, i+1, end, temp)
            temp.pop()
            i += 1


class Solution2:
    """
    backTrace
    """
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        self.dfs(res, nums, 0, [])
        res.sort(key=lambda x: len(x))
        return res

    def dfs(self, res, nums, pos, temp):
        if pos <= len(nums):
            res.append([v for v in temp])
        for i in range(pos, len(nums)):
            if i > pos and nums[i] == nums[i-1]:
                continue
            temp.append(nums[i])
            self.dfs(res, nums, i+1, temp)
            temp.pop()


class Solution3(object):
    """
    https://leetcode.com/problems/subsets-ii/discuss/30305/Simple-python-solution-(DFS).
    """
    def subsetsWithDup(self, nums):
        nums, result, pos = sorted(nums), [[]], {}
        for n in nums:
            start, l = pos.get(n, 0), len(result)
            result += [r + [n] for r in result[start:]]
            pos[n] = l
        return result


class Solution4:
    """
    https://leetcode.com/problems/subsets-ii/discuss/30166/Simple-python-solution-without-extra-space.
    I store the last added items in a list, maybe slightly easier to understand.
    """
    def subsetsWithDup(self, nums):
        if not nums:
            return []
        nums.partition_sort()
        res, cur = [[]], []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                cur = [item + [nums[i]] for item in cur]
            else:
                cur = [item + [nums[i]] for item in res]
            res += cur
        return res


def p_m(m):
    if not m:
        return
    print("*"*10)
    for row in m:
        print(row)


if __name__ == '__main__':
    s = Solution2().subsetsWithDup
    p_m(s([1, 2, 2, 2, 3]))
