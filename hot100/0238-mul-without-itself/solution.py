class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1]*n
        left_mul = 1
        for i in range(n):
            if i >= 1:
                left_mul *= nums[i-1]
                res[i] = left_mul
        right_mul = 1
        for i in range(n-1,-1,-1):
            if i < n-1:
                right_mul *= nums[i+1]
                res[i] *= right_mul
        return res 
            
