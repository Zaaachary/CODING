# -*- encoding: utf-8 -*-
'''
@File    :   0072.hard.!.编辑距离.py
@Time    :   2022/06/25 17:19:54
@Author  :   Zhifeng Li
@Contact :   li_zaaachary@163.com
@Desc    :   
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
                j_1 = dp_matrix[i][j-1]
                i_1 = dp_matrix[i-1][j]
                ij_1 = dp_matrix[i-1][j-1]

                if word2[j-1] == word1[i-1]:
                    dp_matrix[i][j] = 1 + min(j_1, i_1, ij_1 - 1)
                else:
                    dp_matrix[i][j] = 1 + min(j_1, i_1, ij_1)
        
        return dp_matrix[-1][-1]
                    