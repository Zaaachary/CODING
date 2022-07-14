# -*- encoding: utf-8 -*-
'''
@File    :   1049.medium.最后一块石头的重量 II.py
@Time    :   2022/07/14 10:36:14
@Author  :   Zhifeng Li
@Contact :   li_zaaachary@163.com
@Desc    :   https://leetcode.cn/problems/last-stone-weight-ii/
'''

class Solution:
    '''
    执行用时： 76 ms , 在所有 Python3 提交中击败了 40.94% 的用户 内存消耗： 16.4 MB , 在所有 Python3 提交中击败了 5.03% 的用户
    '''
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total_weight = sum(stones)
        bag_size = total_weight // 2
        # print(bag_size)
        dp = [[0] * (bag_size+1) for _ in range(len(stones))]
        for idx in range(stones[0], bag_size+1):
            dp[0][idx] = stones[0]
        # print(dp)
        for i in range(1, len(stones)):
            for j in range(bag_size + 1):
                if stones[i] <= j:
                    dp[i][j] = max(stones[i]+dp[i-1][j-stones[i]], dp[i-1][j])
                else:
                    dp[i][j] = dp[i-1][j]
                # print(dp)

        left_part = total_weight - dp[-1][-1]
        return abs(dp[-1][-1] - left_part)

        # return 0