from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if len(numbers) < 2:
            raise ValueError("no answer")
        l, r = 0, len(numbers)-1
        while l < r:
            v = numbers[l] + numbers[r]
            if v == target:
                return [l+1, r+1]
            elif v > target:
                r -= 1
            else:
                l += 1
        raise ValueError("no answer")
            