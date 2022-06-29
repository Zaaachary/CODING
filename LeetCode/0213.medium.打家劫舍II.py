# -*- encoding: utf-8 -*-
'''
@File    :   0213.medium.打家劫舍II.py
@Time    :   2022/06/26 10:43:46
@Author  :   Zhifeng Li
@Contact :   li_zaaachary@163.com
@Desc    :   
你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都 围成一圈 ，这意味着第一个房屋和最后一个房屋是紧挨着的。同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警 。

给定一个代表每个房屋存放金额的非负整数数组，计算你 在不触动警报装置的情况下 ，今晚能够偷窃到的最高金额。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/house-robber-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List

class Solution:
    '''
    执行用时： 32 ms , 在所有 Python3 提交中击败了 90.18% 的用户 内存消耗： 14.9 MB , 在所有 Python3 提交中击败了 48.15% 的用户
    '''
    def rob(self, nums: List[int]) -> int:
        # 首尾相连的 rob
        if len(nums) == 0:
            return 0
        elif len(nums) <= 2:
            return max(nums)
        else:

            return max(self.compute(nums[:-1]), self.compute(nums[1:]))

    def compute(self, nums):
        # 首尾不相连的 rob
        if len(nums) <= 2:
            return max(nums)
        else:
            dp = [0] * len(nums)
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])
            for idx in range(2, len(nums)):
                dp[idx] = max(dp[idx-1], dp[idx-2]+nums[idx])

        return dp[-1]
