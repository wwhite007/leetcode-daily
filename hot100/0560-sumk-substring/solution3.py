class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count_num = {0: 1}
        prefix_sum = 0
        res = 0

        for num in nums:
            prefix_sum += num

            remain = prefix_sum - k

            if remain in count_num:
                res += count_num[remain]

            if prefix_sum not in count_num:
                count_num[prefix_sum] = 1
            else:
                count_num[prefix_sum] += 1

        return res
