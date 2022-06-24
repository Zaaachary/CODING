# -*- encoding: utf-8 -*-
'''
@File    :   1091.二进制矩阵中的最短路径.py
@Time    :   2022/06/22 16:07:27
@Author  :   Zhifeng Li
@Contact :   li_zaaachary@163.com
@Desc    :   
给你一个 n x n 的二进制矩阵 grid 中，返回矩阵中最短 畅通路径 的长度。如果不存在这样的路径，返回 -1 。

二进制矩阵中的 畅通路径 是一条从 左上角 单元格（即，(0, 0)）到 右下角 单元格（即，(n - 1, n - 1)）的路径，该路径同时满足下述要求：

路径途经的所有单元格都的值都是 0 。
路径中所有相邻的单元格应当在 8 个方向之一 上连通（即，相邻两单元之间彼此不同且共享一条边或者一个角）。
畅通路径的长度 是该路径途经的单元格总数。
'''
from typing import List

class Solution_BFS:
    '''
    执行用时： 324 ms , 在所有 Python3 提交中击败了 58.29% 的用户 内存消耗： 15.1 MB , 在所有 Python3 提交中击败了 95.39% 的用户
    '''
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.n = len(grid)
        if not self.grid[0][0] and not self.grid[-1][-1]:
            return self.BFS()
        else:
            return -1

    def BFS(self):
        current_len = 0
        queue = [(0,0), None]
        while queue:
            temp = queue.pop(0)
            if temp:
                c_i, c_j = temp
            else:
                current_len += 1
                if queue:
                    queue.append(None)
                continue
            if c_i == c_j == self.n -1:
                return current_len + 1
            else:
                for n_i, n_j in [
                    (c_i+1, c_j), (c_i-1, c_j),
                    (c_i, c_j+1), (c_i, c_j-1),
                    (c_i+1, c_j+1), (c_i+1, c_j-1),
                    (c_i-1, c_j+1), (c_i-1, c_j-1),
                    ]:
                    if 0 <= n_i < self.n and 0 <= n_j < self.n \
                        and not self.grid[n_i][n_j]:
                        self.grid[n_i][n_j] = 1
                        queue.append((n_i, n_j))
        return -1

from collections import deque

class Solution_BFS_other:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] != 0:
            return -1
        length = len(grid)
        if length == 1:
            return 1
        que = deque()
        visited = {}
        que.appendleft((0,0))
        visited[(0,0)] = True
        start = 1
        while que:
            for _ in range(len(que)):
                ind, con = que.pop()
                for pos_h, pos_v in [(-1,-1), (-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1)]:
                    new_ind = ind + pos_h
                    new_con = con + pos_v
                    if 0 <= new_ind < length and 0 <= new_con < length and grid[new_ind][new_con] == 0 and not visited.get((new_ind, new_con)):
                        if new_ind == length - 1 and new_con == length - 1:
                            return start + 1
                        que.appendleft((new_ind, new_con))
                        visited[(new_ind, new_con)] = True
            start += 1
        return -1




class Solution_DFS:
    '''
    超时 DFS 回溯
    '''
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.n = len(grid)
        self.min_len = self.n**2 + 1
        self.current_len = 0
        if not self.grid[0][0]:
            self.DFS(0, 0)

        if self.min_len == self.n**2 + 1:
            return -1
        else:
            return self.min_len

        
    def DFS(self, t_i, t_j):
        self.current_len += 1
        self.grid[t_i][t_j] = 1
        if t_i == self.n-1 and t_j == self.n-1:
            self.min_len = min(self.min_len, self.current_len)
        elif self.current_len < self.min_len:
            for n_i, n_j in [(t_i, t_j+1), (t_i, t_j-1), 
                (t_i+1, t_j), (t_i-1, t_j),
                (t_i+1, t_j+1), (t_i-1, t_j-1),
                (t_i+1, t_j-1), (t_i-1, t_j+1),
            ]:
                if 0 <= n_i < self.n and 0 <= n_j < self.n\
                    and not self.grid[n_i][n_j]:
                    self.DFS(n_i, n_j)
        
        self.grid[t_i][t_j] = 0
        self.current_len -= 1