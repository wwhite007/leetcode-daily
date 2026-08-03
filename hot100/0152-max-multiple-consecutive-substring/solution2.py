class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = max_value = min_value = nums[0]
        for i in nums[1:]:

            tmp = max_value
            max_value = max(i, i*max_value, i*min_value)
            min_value = min(i, i*tmp, i*min_value)
                
            if max_value > ans:
                ans =max_value
        return ans
