class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp= []
        for i in range(len(nums)):
            dp.append([])
        dp[0].append(nums[0])
        for i in range(1,len(nums)):
            max_ele = nums[i]
            min_ele = nums[i]
            for j in dp[i-1]:
                if j*nums[i] > max_ele:
                    max_ele = j*nums[i]
                if j*nums[i] < min_ele:
                    min_ele = j*nums[i]
            dp[i].append(max_ele)
            dp[i].append(min_ele)
        max_value = []
        for i in range(0,len(nums)):
            max_value.append(dp[i][0])  
        return max(max_value)

