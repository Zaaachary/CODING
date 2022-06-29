# -*- encoding: utf-8 -*-
'''
@File    :   0062.medium.不同路径.py
@Time    :   2022/06/26 17:00:48
@Author  :   Zhifeng Li
@Contact :   li_zaaachary@163.com
@Desc    :   
'''
from typing import List

class Solution:
    '''
    动态规划
    执行用时： 32 ms , 在所有 Python3 提交中击败了 91.32% 的用户 内存消耗： 14.8 MB , 在所有 Python3 提交中击败了 86.01% 的用户
    '''
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]
        for i in range(0, n):
            dp[0][i] = 1
        for i in range(0, m):
            dp[i][0] = 1
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]