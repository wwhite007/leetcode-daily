class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_pos = []
        for i in range(len(nums)):
            if nums[i] == 0:
                zero_pos.append(i)
                nums.append(0)
        for j in range(len(zero_pos)):
            nums.pop(zero_pos[j]-j)
        return 
