from typing import *
from utils import assert_eq


class Solution:
    def maxProfit(self, prices):
        max_profit, min_price = 0, float('inf')
        for price in prices:
            min_price = min(min_price, price)
            profit = price - min_price
            max_profit = max(max_profit, profit)
        return max_profit


class Solution2:
    """扩展为找到买卖的日期"""
    def maxProfit(self, prices):
        max_profit, min_price = 0, float('inf')
        buy_in_index, sell_out_index = -1, -1
        for index, price in enumerate(prices):
            if price < min_price:
                buy_in_index = index
                min_price = price
            profit = price - min_price
            if profit > max_profit:
                max_profit = profit
                sell_out_index = index
            max_profit = max(max_profit, profit)
        return buy_in_index, sell_out_index, max_profit


if __name__ == '__main__':
    s = Solution2().maxProfit
    # assert_eq(s([7,1,5,3,6,4]), 5)
    print(s([7,1,5,3,6,4]))