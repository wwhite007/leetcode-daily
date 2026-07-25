比较标准的dp
子问题是针对nums[0:i]的子列表
但是这里的循环起止条件很重要，最后的目标一定是dp[len(nums)]，因此上面的循环应该是for i in range(1, len(nums)+1)
这种细节需要处理好，不然就会因为dp[0],dp[len(nums-1)]这种傻逼问题而犯错。
