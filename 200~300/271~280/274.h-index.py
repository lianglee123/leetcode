from typing import *


"""
三步解法，逐步化解
"""


class Solution1:
    """
    遇到不会或者不理解的题，应该先把暴力的做法写出，
    这样才能确认自己理解了。
    https://leetcode-cn.com/problems/h-index/solution/san-chong-jie-fa-zhu-bu-you-hua-by-youngfolk/
    """
    def hIndex(self, citations: List[int]):
        n = len(citations)
        ans = 0
        for i in range(n+1):  # i是我们试探的h
            temp = 0
            for c in citations: # temp是引用数大于h的所有论文数
                if c >= i:
                    temp += 1
            if temp >= i:
                ans = max(ans, i)
        return ans


class Solution2:
    """
    排序后再查找，其实要查找的是citations[i] >= n-i， 返回最小的i
    """
    def hIndex(self, citations: List[int]):
        if not citations: return 0
        n = len(citations)
        for i in range(n):
            if citations[i] >= n-i:  # 因为排过序了，所以不用在想第一步那样求temp
                return n - i
        return 0


class Solution3:
    """
    继续使用二分法搜素
    """
    def hIndex(self, citations: List[int]):
        citations.sort()
        n  = len(citations)
        if not citations or citations[-1] == 0:
            return 0
        l, r = 0, n-1
        while l < r:
            mid = l + (r-l)//2
            if citations[mid] >= n - mid:
                r = mid
            else:
                l = mid + 1

        return n -l

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



