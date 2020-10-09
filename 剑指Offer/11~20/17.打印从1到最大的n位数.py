from typing import *



class Solution:
    def printNumbers(self, n: int) -> List[str]:
        if n == 0:
            return []
        res = []
        nums = [''] * n
        self.dfs(res, nums, 0)
        res[0] = "0"
        return res[1:]

    def dfs(self, res, nums, n):
        if n == len(nums):
            res.append("".join(nums).lstrip("0"))
            return
        for i in range(10):
            nums[n] = str(i)
            self.dfs(res, nums, n+1)


class Solution2:
    def printNumbers(self, n: int) -> List[int]:
        return list(range(n))
if __name__ == '__main__':
    s = Solution().printNumbers
    print(s(0))
    print(s(1))
    print(s(2))
