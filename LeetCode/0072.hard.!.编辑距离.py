# -*- encoding: utf-8 -*-
'''
@File    :   0072.hard.!.编辑距离.py
@Time    :   2022/06/25 17:19:54
@Author  :   Zhifeng Li
@Contact :   li_zaaachary@163.com
@Desc    :   

在单词 A 中插入一个字符；
在单词 B 中插入一个字符；
修改单词 A 的一个字符。

'''

class Solution:
    '''
    执行用时： 140 ms , 在所有 Python3 提交中击败了 89.32% 的用户 内存消耗： 18.8 MB , 在所有 Python3 提交中击败了 39.06% 的用户
    '''
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)

        dp_matrix = [[0 for _ in range(n+1)] for _ in range(m+1)]
        
        for idx in range(m+1):
            dp_matrix[idx][0] = idx
        
        for idx in range(n+1):
            dp_matrix[0][idx] = idx

        for i in range(1, m+1):
            for j in range(1, n+1):
                j_1 = dp_matrix[i][j-1]     # 字符1 <-> 字符2[:-1] 编辑距离，接下来可做插入
                i_1 = dp_matrix[i-1][j]     # 字符1[:-1] <-> 字符2 编辑距离，接下来可做插入
                ij_1 = dp_matrix[i-1][j-1]  # 字符1[:-1] <-> 字符2[:-1] 编辑距离，接下来可做新字符交换

                if word2[j-1] == word1[i-1]:
                    dp_matrix[i][j] = min(j_1 + 1, i_1 + 1, ij_1)
                else:
                    dp_matrix[i][j] = 1 + min(j_1, i_1, ij_1)
        
        return dp_matrix[-1][-1]

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0] * (len(word2)+1) for _ in range(len(word1)+1)]
        for i in range(len(word1)+1):
            dp[i][0] = i
        for j in range(len(word2)+1):
            dp[0][j] = j
        for i in range(1, len(word1)+1):
            for j in range(1, len(word2)+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
        return dp[-1][-1]

from functools import cache

class Solution_memory:
    '''
    记忆化搜索
    执行用时： 756 ms , 在所有 Python3 提交中击败了 5.16% 的用户 内存消耗： 126.1 MB , 在所有 Python3 提交中击败了 5.01% 的用户
    '''
    @cache
    def minDistance(self, word1: str, word2: str) -> int:
        if word1 == word2:
            return 0
        elif not word1:
            return len(word2)
        elif not word2:
            return len(word1)
        
        mid_1 = self.minDistance(word1[:-1], word2) 
        mid_2 = self.minDistance(word1, word2[:-1])
        mid_3 = self.minDistance(word1[:-1], word2[:-1])
        if word1[-1] == word2[-1]:
            return 1 + min(mid_1, mid_2, mid_3 - 1)
        else:
            return 1 + min(mid_1, mid_2, mid_3)
