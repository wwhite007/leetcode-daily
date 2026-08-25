class Solution:
    def jump(self, nums: List[int]) -> int:

        steps = 0
        end = 0
        max_position = 0

        for i in range(len(nums)-1):

            # 当前点可以达到的最远位置
            max_position = max(
                max_position,
                i + nums[i]
            )

            # 到达当前跳跃边界
            if i == end:

                steps += 1

                # 更新下一跳边界
                end = max_position


        return steps
