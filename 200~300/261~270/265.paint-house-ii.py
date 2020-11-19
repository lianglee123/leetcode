from typing import *


class Solution:
    """
    先使用dp暴力解决，之后发掘在找最小值的是时候太过于暴力了
    这题除了DP还有一个关键点是，如何快速一个数组求出除了自身以外的最小值
    答：如果该值是最小值，那么返回第二小的值，其他情况都返回最小值。
    详情请见，solution2
    """
    def minCost(self, costs: List[List[int]]):
        if not costs and not costs[0]:
            return 0
        size = len(costs)
        k = len(costs[0])
        sumCost = costs[0][:]
        for i in range(1, size):
            cost = costs[i]
            newSumCost = []
            for j in range(k):
                newSumCost.append(sumCost[j] + min(min(cost[0:j]), min(cost[j+1:])))
            sumCost = newSumCost
        return min(sumCost)


class Solution2:
    """
    https://blog.csdn.net/qq508618087/article/details/50807874
    """
    def minCost(self, costs: List[List[int]]):
        if not costs and not costs[0]:
            return 0
        if len(costs[0]) == 1:
            return sum(cost[0] for cost in costs)

        n = len(costs)
        k = len(costs[0])
        sumCost = costs[0][:]
        for i in range(1, n):
            min1, min1Index, min2, _ = self.minInfo(costs[i])
            newSumCost = []
            for j in range(k):
                if j == min1Index:
                    newSumCost.append(sumCost[j] + min2)
                else:
                    newSumCost.append(sumCost[j] + min1)
        return min(sumCost)

    def minInfo(self, cost):
        min1, min2 = cost[0], cost[1]
        min1Index, min2Index = 0, 1
        if min2 < min1:
            min1, min2 = min2, min1
            min1Index, min2Index = min2Index, min1Index
        for i in range(2, len(cost)):
            if cost[i] <= min1:
                min11, min1Index, min2, min2Index = cost[i], i, min1, min1Index
            elif cost[i] <= min2:
                min2, min2Index = cost[i], i
        return min1, min1Index, min2, min2Index


