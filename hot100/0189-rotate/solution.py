class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ans = [0] * len(nums)
        for i in range(len(nums)):
            j = (k+i)%len(nums)
            ans[j] = nums[i]
        nums[:] = ans
