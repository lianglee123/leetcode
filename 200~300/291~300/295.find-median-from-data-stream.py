from typing import *


from heapq import *


class MedianFinder:
    """
    https://blog.csdn.net/da_kao_la/article/details/100636473
    当想不到做法时，就从最暴力的角度想去。然后桌布优化。一开始就想找个很好的方法，而
    拒绝思考暴力的方法的思路，也有可能变成你无法接触提的绊脚石。
    """
    def __init__(self):
        self.smallParts = [] # 最大堆
        self.largeParts = [] # 最小堆,堆顶是最小值

    def addNums(self, num):
        smallval = heappushpop(self.largeParts, num)
        heappush(self.smallParts, -smallval)
        if len(self.largeParts) < len(self.smallParts):
            heappush(self.largeParts, -heappop(self.smallParts))

    def findMedian(self):
        if len(self.largeParts) > len(self.smallParts):
            return float(self.largeParts[0])
        return (self.largeParts[0] - self.smallParts[0]) / 2.0
