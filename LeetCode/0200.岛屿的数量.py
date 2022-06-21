# -*- encoding: utf-8 -*-
'''
@File    :   0200.岛屿的数量.py
@Time    :   2022/06/20 15:27:23
@Author  :   Zhifeng Li
@Contact :   li_zaaachary@163.com
@Desc    :   

给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。

岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。

此外，你可以假设该网格的四条边均被水包围。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/number-of-islands
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    '''
    执行用时： 164 ms , 在所有 Python3 提交中击败了 15.15% 的用户 内存消耗： 24 MB , 在所有 Python3 提交中击败了 41.09% 的用户
    '''
    def numIslands(self, grid: List[List[str]]) -> int:
        self.grid = grid
        self.m = len(grid)
        self.n = len(grid[0])
        result = 0
        for i in range(self.m):
            for j in range(self.n):
                if self.grid[i][j] == '1':
                    result += 1
                    self.BFS(i, j)

        return result

    def BFS(self, i, j):
        stack = [(i, j)]
        while stack:
            c_i, c_j = stack.pop()
            self.grid[c_i][c_j] = '0'
            for i, j in [[+1, 0], [-1, 0], [0, +1], [0, -1]]:
                t_i = c_i + i
                t_j = c_j + j
                if 0 <= t_i < self.m and 0 <= t_j < self.n \
                    and self.grid[t_i][t_j] == '1':
                    stack.append((t_i, t_j))
        
                    

