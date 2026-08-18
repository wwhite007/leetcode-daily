class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        sum_list = []
        count_num = {}
        res = 0
        for i in range(n):
            if i == 0:
                sum_list.append(nums[i])
            else:
                sum_list.append(sum_list[i-1]+nums[i])
            remain = sum_list[i] - k
            if remain == 0:
                res += 1
            if remain in count_num:
                res += count_num[remain]
            if sum_list[i] not in count_num:
                count_num[sum_list[i]] = 1
            else:
                count_num[sum_list[i]] += 1
        return res


