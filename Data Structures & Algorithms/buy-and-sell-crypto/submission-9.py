class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        l = 0
        best = 0
        for r in range(1, n):
            potential_win = prices[r] - prices[l]
            if potential_win < 0:
                l = r
            else:
                best = max(best, potential_win)
        return best