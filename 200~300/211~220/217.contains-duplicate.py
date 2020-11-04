from typing import *

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set()
        for i, n in enumerate(nums):
            s.add(n)
            if len(s) != i+1:
                return True
        return False
