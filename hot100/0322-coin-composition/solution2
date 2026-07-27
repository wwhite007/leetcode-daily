class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1] * (amount+1)
        dp[0] = 0
        for i in range(1, amount+1):
            for j in coins:
                if j <= i and dp[i-j] + 1 < dp[i]:
                    dp[i] = dp[i-j] + 1
        if dp[amount] > amount:
            return -1
        else:
            return dp[amount]
