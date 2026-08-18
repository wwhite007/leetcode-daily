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
            if sum_list[i] not in count_num:
                count_num[sum_list[i]] = [i]
            else:
                count_num[sum_list[i]].append(i)
        for j in range(n):
            if sum_list[j] == k:
                res += 1
            remain = -k + sum_list[j]
            if remain in count_num:
                for i in count_num[remain]:
                    if i < j:
                        res += 1
                    else:
                        break
        return res


