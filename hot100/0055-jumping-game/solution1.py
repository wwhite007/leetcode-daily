class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False]*n
        dp[0] = True
        for i in range(n-1):
            if nums[i] == 0:
                continue
            elif dp[i] == True:
                for step in range(1,nums[i]+1):
                    if i+step < n:
                        dp[i+step] = True
                        if i+step == n-1:
                            return True
        return dp[n-1]
        
