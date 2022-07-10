# -*- encoding: utf-8 -*-
'''
@File    :   0746.easy.使用最小花费爬楼梯.py
@Time    :   2022/07/08 16:16:24
@Author  :   Zhifeng Li
@Contact :   li_zaaachary@163.com
@Desc    :   
'''

class Solution_v1:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        '''
        执行用时： 44 ms , 在所有 Python3 提交中击败了 55.80% 的用户 内存消耗： 15.1 MB , 在所有 Python3 提交中击败了 9.30% 的用户
        dp: 到第i层需要的最低花费
        顶层为 len(cost) + 1 
        dp[0] = dp[1] = 0 因为可以从 0 和 1 下标开始爬楼
        '''
        if len(cost) < 2:
            return 0
        dp = [0] * (len(cost) + 1)
        # print(dp)
        for i in range(2, len(cost)+1):
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
            # print(dp)
        
        return dp[-1]


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        '''
        执行用时： 32 ms , 在所有 Python3 提交中击败了 97.96% 的用户 内存消耗： 15.1 MB , 在所有 Python3 提交中击败了 33.91% 的用户
        顶层为 len(cost) + 1 
        dp[0] = dp[1] = 0 因为可以从 0 和 1 下标开始爬楼
        '''
        if len(cost) < 2:
            return 0
        s2, s1 = 0, 0
        for i in range(2, len(cost)+1):
            s2, s1 = s1, min(s2 + cost[i-2], s1 + cost[i-1])
        
        return s1