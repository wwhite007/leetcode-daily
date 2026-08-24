class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [0]*n   # 我这里设置成这个点能产生的最大收益
        base = prices[0]
        for i in range(1,n):
            print(dp)
            if prices[i] < base:
                base = prices[i]
            if prices[i] > prices[i-1]:
                dp[i] = max(dp[i-1]+prices[i]-prices[i-1],prices[i]-base)
        return max(dp)
            
