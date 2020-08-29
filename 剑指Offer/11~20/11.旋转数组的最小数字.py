from typing import *

class Solution:
    def minArray(self, numbers: List[int]) -> int:
        l, r = 0, len(numbers)-1
        while l < r:
            mid = (l+r)//2
            if numbers[mid] < numbers[r]:
                r = mid
            elif numbers[mid] > numbers[r]:
                l = mid + 1
            else:
                r -= 1
        return numbers[l]

if __name__ == '__main__':
    s = Solution().minArray
    print(s([3, 4, 5, 1, 2]))
    print(s([2, 2, 2, 0, 1]))