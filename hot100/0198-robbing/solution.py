class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = {}  #这里储存num[0:i]的子序列中可以拿到的最高金额。
        for i in range(1, len(nums)+1):
            if i == 1:
                dp[i] = nums[0]
            elif i == 2:
                dp[i] = max(nums[0], nums[1])
            else:
                dp[i] = max(dp[i-1], dp[i-2] + nums[i-1])
        return dp[len(nums)]
