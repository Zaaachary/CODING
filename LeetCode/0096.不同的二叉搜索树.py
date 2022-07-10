# -*- encoding: utf-8 -*-
'''
@File    :   0096.不同的二叉搜索树.py
@Time    :   2022/07/08 22:48:08
@Author  :   Zhifeng Li
@Contact :   li_zaaachary@163.com
@Desc    :   
https://leetcode.cn/problems/unique-binary-search-trees/
'''

class Solution:
    def numTrees(self, n: int) -> int:
        '''
        执行用时： 24 ms , 在所有 Python3 提交中击败了 99.51% 的用户 内存消耗： 14.9 MB , 在所有 Python3 提交中击败了 27.08% 的用户
        dp[n]
        for i in range(n):
            dp[n] +=  dp[i] * dp[n-i]
        '''
        if n < 1:
            return 0
        
        dp = [0] * (n + 1)   # dp[i] i 个节点可以构成的二叉搜索树数量
        dp[0], dp[1] = 1, 1
        for i in range(2, n + 1):
            for j in range(1, i+1):
                # i个节点中，第j个节点为根的情况
                dp[i] += dp[j-1] * dp[i-j]  # j左边节点的可能数 * j右边节点的可能数

        return dp[-1]