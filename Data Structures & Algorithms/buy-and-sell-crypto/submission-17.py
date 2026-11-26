class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        l, r = 0, 1
        profit = 0
        while r<n:
            curr_profit = prices[r] - prices[l]
            if curr_profit < 0:
                l = r
                r += 1
            else:
                r += 1
            profit = max(profit, curr_profit)
        if profit > 0:
            return profit
        return 0
