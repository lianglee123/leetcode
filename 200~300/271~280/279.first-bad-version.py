from typing import *

def isBadVersion(version) -> bool:
    return True


class Solution:
    def firstBadVersion(self, n):
        l, r = 1, n
        while l < r:
            mid = l + (r-l)//2
            if isBadVersion(mid):
                r = mid
            else:
                l = mid + 1
        return l



