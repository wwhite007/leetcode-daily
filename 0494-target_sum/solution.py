class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        min_num = min(nums)
        sum_num = sum(nums)

        if (sum_num + target)%2 == 1 or abs(target) > sum_num:
            return 0     
        cap = (sum_num + target)//2
        dp = [0] * (cap+1) # 我这里写出来凑出正数和的方法
        dp[0] = 1
        for num in nums:
            for i in range(cap,num-1,-1):
                dp[i] += dp[i-num]

        return dp[cap]
