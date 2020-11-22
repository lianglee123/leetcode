from typing import *


class Solution4:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        n = len(citations)
        if n==0 or citations[-1]==0:
            return 0
        l,r = 0,n-1
        while l<=r:
            mid = l+(r-l)//2
            if citations[mid]>=n-mid:
                r = mid-1
            else:
                l = mid+1
        return n-l
