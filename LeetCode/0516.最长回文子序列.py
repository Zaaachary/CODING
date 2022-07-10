# -*- encoding: utf-8 -*-
'''
@File    :   0516.最长回文子序列.py
@Time    :   2022/07/08 13:03:53
@Author  :   Zhifeng Li
@Contact :   li_zaaachary@163.com
@Desc    :   
https://leetcode.cn/problems/longest-palindromic-subsequence/
'''
# from pprint import pprint

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        '''
        执行用时： 1252 ms , 在所有 Python3 提交中击败了 56.45% 的用户 内存消耗： 31.3 MB , 在所有 Python3 提交中击败了 46.28% 的用户
        dp: s[i:j+1] 中最长的回文子序列
        1, s[i] == s[j]
            dp[i][j] = dp[i+1][j-1] + 2
        2. s[i] != s[j]
            dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        '''
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1

        for r in range(1, n):
            for i in range(n-r):
                j = i + r
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])

        return dp[0][-1]

class Solution_2:
    '''
    从下向上遍历
    '''
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        return dp[0][n - 1]