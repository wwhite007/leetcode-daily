class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        profit = 0 
        base = prices[0]
        for i in range(1,n):
            if prices[i] < base:
                base = prices[i]
            elif prices[i]-base > profit:
                profit = prices[i]-base
        return profit
