class Solution:
    """
    I think this problem's key point is that we want to find the largest number, which num*num <= x,
     therefore we should use the binary search to find the upper bound within the range(1,x).
    """
    def mySqrt(self, x):
        left, right = 0, x
        while True:
            mid = left + (left + right) // 2
            if mid > x // mid:
                right = mid - 1
            else:
                if mid + 1 > x//(mid + 1):
                    return mid
                left = mid + 1



class Solution2:
    """
    I think this problem's key point is that we want to find the largest number, which num*num <= x,
    therefore we should use the binary search to find the upper bound within the range(1,x).
"""

    def mySqrt(self, x):
        l, r = 1, x
        ans = 0
        while l < r:
            mid = l + (r - l)//2
            if mid <= x//mid:
                l = mid + 1
                ans = mid
            else:
                r = mid - 1
        return ans

