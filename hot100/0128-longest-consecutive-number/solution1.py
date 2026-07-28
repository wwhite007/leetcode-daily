class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ordered_nums = sorted(list(set(nums)))
        index = {}
        if len(nums) == 0:
            return 0
        max_len = 1
        for i in range(len(ordered_nums)):
            if ordered_nums[i]-i not in index:
                index[ordered_nums[i]-i] = 1
            else:
                index[ordered_nums[i]-i] += 1
                if index[ordered_nums[i]-i] > max_len:
                    max_len = index[ordered_nums[i]-i]
        return max_len
        
