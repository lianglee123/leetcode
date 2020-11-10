from typing import *




class Solution:
    def isStrobogrammatic(self, num):
        if not num:
            return False
        l, r = 0, len(num)-1
        while l <= r:
            if num[l] == num[r]:
                if num[l] not in '018':
                    return False
            else:
                if num[l] + num[r] not in ('69', '96'):
                    return False
            l += 1
            r -= 1
        return True

