class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        buy, best = 0, 0
        for sell in range(1, n):
            potential_profit = prices[sell] - prices[buy]
            while potential_profit < 0 and buy < sell:
                buy += 1
            else:
                best = max(best, potential_profit)
        return best