class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tail = []
        def find_index(l, ele): 
            #binary search 
            left = 0
            right = len(l)
            while left < right:
                mid = (left + right) // 2
                if l[mid] < ele:
                    left = mid +1
                else:
                    right = mid
            return left
        for num in nums:
            idx = find_index(tail, num)
            if idx == len(tail):
                tail.append(num)
            else:
                tail[idx] = num
        return len(tail)
