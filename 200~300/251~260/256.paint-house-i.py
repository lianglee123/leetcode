from typing import *


class Solution:
    """
    https://www.cnblogs.com/grandyang/p/5319384.html
    扩展：如果要求返回粉刷方案该怎么办？
    """
    def minCost(self, costs: List[List]):
        if not costs or not costs[0]:
            return 0
        preR, preB, preG = costs[0]
        for i in range(1, len(costs)):
            tmpR, tmpB, tmpG = costs[i]
            curR = tmpR + min(preB, preG)
            curB = tmpB + min(preR, preG)
            curG = tmpG + min(preR, preB)
            preR, preB, preG = curR, curB, curG
        return min(preR, preB, preG)


