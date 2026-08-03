# 找下限插入
def lower_bound(nums, target):
    left, right = 0, len(nums)

    while left < right:
        mid = (left + right) // 2

        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid

    return left
这里是找到第一个大于等于target位置的模板。
