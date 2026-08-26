class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water = 0
        n = len(height)
        left, right = 0, n-1
        while left < right:
            if height[left] > height[right]:
                current_water = (right-left)*height[right]
                right -= 1
            else:
                current_water = (right-left)*height[left]
                left += 1                
            if current_water > max_water:
                max_water = current_water
        return max_water
