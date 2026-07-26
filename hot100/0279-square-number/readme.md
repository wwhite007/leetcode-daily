我一开始打算用这个方法：
class Solution:
    def numSquares(self, n: int) -> int:
        dp = {} # dp[i]用来记录数字i对应的完全平方数的最少数量
        for i in range(1, n+1):
            dp[0] = 0  
            if i == 1:
                dp[i] = 1
            else:
                for j in range(1, int(i**0.5)+1):
                    if j == 1:
                        dp[i] = dp[i-1] + 1
                    else:
                        dp[i] = min(dp[i], dp[i-j**2]+1)
        return dp[n]
但是缺点是需要用O(N**2)

