

class Solution:
    def maxProfit(self, prices):
        if len(prices) <= 1:
            return 0
        maxLeftDP = [None] * len(prices)
        maxLeftDP[0] = 0
        minLeft = prices[0]
        for i, p in enumerate(prices[1:]):
            minLeft = min(min, p)
            maxLeftDP[i] = prices[i] - minLeft

        maxRight = 0
        ans = 0
        i = len(prices) - 1
        value = 0
        while i >= 0:
            maxRight = max(prices[i], maxRight)
            value = max(value, maxRight-prices[i])
            if i == 0:
                ans = max(ans, value)
            else:
                ans = max(ans, maxLeftDP[i-1]+value)
            i -= 1
        return ans