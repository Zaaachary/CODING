# -*- encoding: utf-8 -*-
'''
@File    :   0695.medium.岛屿的最大面积.py
@Time    :   2022/03/03 15:18:41
@Author  :   Zhifeng Li
@Contact :   li_zaaachary@163.com
@Desc    :   
给你一个大小为 m x n 的二进制矩阵 grid 。

岛屿 是由一些相邻的 1 (代表土地) 构成的组合，这里的「相邻」要求两个 1 必须在 水平或者竖直的四个方向上 相邻。你可以假设 grid 的四个边缘都被 0（代表水）包围着。

岛屿的面积是岛上值为 1 的单元格的数目。

计算并返回 grid 中最大的岛屿面积。如果没有岛屿，则返回面积为 0 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/max-area-of-island
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from collections import deque
from typing import List

class Solution:
    '''
    作者：LeetCode-Solution
    链接：https://leetcode-cn.com/problems/max-area-of-island/solution/dao-yu-de-zui-da-mian-ji-by-leetcode-solution/
    来源：力扣（LeetCode）
    著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    '''
    def dfs(self, grid, cur_i, cur_j) -> int:
        if cur_i < 0 or cur_j < 0 or cur_i == len(grid) or cur_j == len(grid[0]) or grid[cur_i][cur_j] != 1:
            return 0
        grid[cur_i][cur_j] = 0
        ans = 1
        for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            next_i, next_j = cur_i + di, cur_j + dj
            ans += self.dfs(grid, next_i, next_j)
        return ans

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        for i, l in enumerate(grid):
            for j, n in enumerate(l):
                ans = max(self.dfs(grid, i, j), ans)
        return ans

class Solution:
    '''
    88ms 32.77%  使用visited，即不改变岛屿的值
    优化：可以使用岛屿的值 替代visited 访问过的置0即可
    '''
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        self.m, self.n = len(grid), len(grid[0])
        self.grid = grid
        self.visited = [[False for _ in range(self.n)]for _ in range(self.m)]
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] and not self.visited[i][j]:
                    cur_area = self.BFS(i, j)
                    max_area = max(max_area, cur_area)
        return max_area
    
    def BFS(self, x, y):
        area = 0
        queue = deque()
        queue.appendleft((x, y))
        self.visited[x][y] = True
        direction = ((1,0), (-1, 0), (0, 1), (0, -1))
        while queue:
            cur_x, cur_y = queue.pop()
            area += 1
            for i, j in direction:
                tmp_x = cur_x + i
                tmp_y = cur_y + j
                if 0 <= tmp_x < self.m and 0 <= tmp_y < self.n \
                    and self.grid[tmp_x][tmp_y] and not self.visited[tmp_x][tmp_y]:
                    queue.appendleft((tmp_x, tmp_y))
                    self.visited[tmp_x][tmp_y] = True

        return area
            
if __name__ == "__main__":
    target = [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]
    S = Solution()
    print(S.maxAreaOfIsland(target))
