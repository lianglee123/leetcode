from typing import *

class Solution:
    """
    解决方法是，把a,b分割到不同的数组中
    https://segmentfault.com/a/1190000004886431
    """
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for n in nums:
            xor ^= n
        mask = 1
        while xor & mask == 0:
            mask = mask << 1
        a, b = 0, 0
        for num in nums:
            if num & mask == 0:
                a ^= num
            else:
                b ^= num
        return [a, b]
