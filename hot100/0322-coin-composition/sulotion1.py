class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}  # 代表当前的sum是i的时候，最后的结果是dp[i].
        dp[0] = 0 
        for i in range(0, amount+1):
            if i == 0:
                dp[i] = 0
            elif i < min(coins):
                dp[i] = amount+1
            else:
                for j in coins:
                    if i < j:
                        continue
                    elif i not in dp:
                        dp[i] = dp[i-j] + 1
                    else:
                        if j <= i:
                            dp[i] = min(dp[i], dp[i-j]+1)
        if dp[amount] > amount:
            return -1
        else:
            return dp[amount] 

        
