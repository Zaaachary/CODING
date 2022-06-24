# -*- encoding: utf-8 -*-
'''
@File    :   0130.medium.被围绕的区域.py
@Time    :   2022/06/22 16:50:36
@Author  :   Zhifeng Li
@Contact :   li_zaaachary@163.com
@Desc    :   
给你一个 m x n 的矩阵 board ，由若干字符 'X' 和 'O' ，找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。
'''
from typing import List

from collections import deque

class Solution:
    '''
    将所有O标为?，从边缘的O开始广度优先遍历。 
    执行用时： 48 ms , 在所有 Python3 提交中击败了 69.02% 的用户 内存消耗： 18.5 MB , 在所有 Python3 提交中击败了 91.52% 的用户
    '''
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])

        queue = deque()
        for i in range(m):
            if board[i][0] == 'O':
                queue.append((i,0))
            if board[i][n-1] == "O":
                queue.append((i,n-1))
        for j in range(n):
            if board[0][i] == 'O':
                queue.append((0,1))
            if board[m-1][i] == 'O':
                queue.append((m-1,1))

        direct = ((+1, 0), (-1, 0), (0, +1), (0, -1))
        while queue:
            i, j = queue.popleft()
            board[i][j] = 'B'
            for t_i, t_j in direct:
                c_i = t_i + i
                c_j = t_j + j
                if 0 <= c_i < m and 0 <= c_j < n \
                    and board[c_i][c_j] == 'O':
                    queue.append((c_i, c_j))
    
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'B':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'

        