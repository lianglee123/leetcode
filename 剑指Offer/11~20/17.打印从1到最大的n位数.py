from typing import *



class Solution:
    def printNumbers(self, n: int) -> List[str]:
        if n == 0:
            return []
        res = []
        nums = [0] * n
        self.dfs(res, nums, 0)
        res[0] = "0"
        return res

    def dfs(self, res, nums, n):
        if len(nums) == n:
            res.append("".join(nums).lstrip("0"))
            return
        for i in range(10):
            nums[n] = str(i)
            self.dfs(res, nums, n+1)


if __name__ == '__main__':
    s = Solution().printNumbers
    print(s(0))
    print(s(1))
    print(s(2))
