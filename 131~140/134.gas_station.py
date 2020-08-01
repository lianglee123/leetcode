from typing import List


class Solution:
    """
    https://www.cnblogs.com/grandyang/p/4266812.html
    我的证明思路：
    通过gas[i]-cost[i]得到一个正负数的数组，记为step[i]，数组中的每一数表示从当前走能否走到下一步。
    遍历step, 把相邻数相加值大于等于0的数合并，后可能会只剩两三个，最后不能合并的是负数大于整数的数组对。
    如果sum(gas)-sum(cost)>=0 那么最后肯定只能合并为一个大于等于零的数。此时一定存在一个方案。
    """
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        sumGas = 0
        sumCost = 0
        start = 0
        tank = 0
        for i in range(len(gas)):
            sumGas += gas[i]
            sumCost += cost[i]
            tank += (gas[i] - cost[i])
            if tank < 0:
                start = i + 1
                tank = 0
        return  -1 if sumGas < sumCost else start
