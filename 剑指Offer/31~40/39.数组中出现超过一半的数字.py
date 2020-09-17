from typing import *


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = None
        count = 0
        for n in nums:
            if count == 0:
                majority = n
            if n == majority:
                count += 1
            else:
                count -= 1
        return majority

class Solution2:
    def majorityElement(self, nums: List[int]) -> int:
        majority = nums[0]
        count = 1
        for n in nums[1:]:
            if majority == n:
                count += 1
            else:
                count -= 1
                if count < 0:
                    count = 1
                    majority = n
        return majority


if __name__ == '__main__':
    s = Solution2().majorityElement
    print(s([1, 2, 3, 2, 2, 2, 5, 4, 2]))
    print(s([47,47,72,47,72,47,79,47,12,92,13,47,47,83,33,
             15,18,47,47,47,47,64,47,65,47,47,47,47,70,47,
             47,55,47,15,60,47,47,47,47,47,46,30,58,59,47,
             47,47,47,47,90,64,37,20,47,100,84,47,47,47,47,
             47,89,47,36,47,60,47,18,47,34,47,47,47,47,47,
             22,47,54,30,11,47,47,86,47,55,40,49,34,19,67,
             16,47,36,47,41,19,80,47,47,27]))
    a = [47,47,72,47,72,47,79,47,12,92,13,47,47,83,33,
         15,18,47,47,47,47,64,47,65,47,47,47,47,70,47,
         47,55,47,15,60,47,47,47,47,47,46,30,58,59,47,
         47,47,47,47,90,64,37,20,47,100,84,47,47,47,47,
         47,89,47,36,47,60,47,18,47,34,47,47,47,47,47,
         22,47,54,30,11,47,47,86,47,55,40,49,34,19,67,
         16,47,36,47,41,19,80,47,47,27]
    a.sort()
    print(a)
    print(len(a), a.count(47))

