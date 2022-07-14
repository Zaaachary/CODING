# -*- encoding: utf-8 -*-
'''
@File    :   0010.hard.正则表达式匹配.py
@Time    :   2022/07/14 10:12:18
@Author  :   Zhifeng Li
@Contact :   li_zaaachary@163.com
@Desc    :   https://leetcode.cn/problems/regular-expression-matching/
'''

class Solution:
    '''
    执行用时： 60 ms , 在所有 Python3 提交中击败了 38.44% 的用户 内存消耗： 15.1 MB , 在所有 Python3 提交中击败了 30.89% 的用户
    '''
    def isMatch(self, s: str, p: str) -> bool:
        if p == '.*':
            return True
        m, n = len(s), len(p)

        def matches(i: int, j: int) -> bool:
            # s == empty
            if i == 0:
                return False
            # s[j] is .
            if p[j - 1] == '.':
                return True
            return s[i - 1] == p[j - 1]

        dp = [[False] * (n+1) for _ in range(m + 1)]
        dp[0][0] = True
        print(dp)

        for i in range(m + 1):
            # s[0~i]
            for j in range(1, n + 1):
                # p[0~j]
                if p[j - 1] != '*':     # j 1~n+1  因需-1
                    if matches(i, j):
                        dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i][j - 2]   # 不使用当前 x*
                    if matches(i, j - 1):
                        dp[i][j] |= dp[i-1][j]
                print(i,j, dp)
        return dp[-1][-1]
