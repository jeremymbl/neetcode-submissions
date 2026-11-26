class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        n = len(prices)
        for i in range(1, n):
            for j in range(i):
                profit = prices[i] - prices[j]
                maxProfit = max(profit, maxProfit)
        return maxProfit
