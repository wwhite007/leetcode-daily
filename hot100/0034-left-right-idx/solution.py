class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def find_idx(left, right ,nums, target):
            while left < right:
                mid = (left + right)//2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid
            return left
        left_idx = find_idx(0, len(nums) ,nums, target)
        right_idx = find_idx(0, len(nums) ,nums, target+1)-1
        if left_idx > right_idx:
            return [-1,-1]
        return [left_idx,right_idx]        
