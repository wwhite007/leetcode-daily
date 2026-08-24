class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        right = 0
        for i in range(n-1):
            if i <= right and nums[i] + i > right:
                right = nums[i] + i
            if right >= n-1:
                return True
        return right >= n-1
        
