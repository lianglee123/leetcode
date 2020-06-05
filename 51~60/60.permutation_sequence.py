import math

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        per = ''
        nums = list(range(1, n+1))
        k -= 1 # 1 index base to 0 index base
        while n > 0:
            n -= 1
            index, k = divmod(k, math.factorial(n))
            per += str(nums[index])
            nums.remove(nums[index])



