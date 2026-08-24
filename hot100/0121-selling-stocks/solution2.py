class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        profit = 0 
        base = prices[0]
        for price in prices:
            
            base = min(price,base)
            profit = max(profit,price-base)
        return profit
            
