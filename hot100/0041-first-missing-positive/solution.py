class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        if 1 not in nums:
            return 1
        for i in range(1,n):
            if nums[i] > 1 and nums[i-1] < nums[i]-1:
                return nums[i-1]+1
        return nums[n-1]+1
