# -*- encoding: utf-8 -*-
'''
@File    :   0063.不同路径II.py
@Time    :   2022/07/08 20:22:05
@Author  :   Zhifeng Li
@Contact :   li_zaaachary@163.com
@Desc    :   
https://leetcode.cn/problems/unique-paths-ii/
特点：机器人只往两个方向移动
'''

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        '''
        执行用时： 36 ms , 在所有 Python3 提交中击败了 78.16% 的用户 内存消耗： 15.3 MB , 在所有 Python3 提交中击败了 5.20% 的用户
        dp: 到 i,j 处的路线数量
        初始条件应避开障碍物
        if i,j 障碍物
            dp[i][j] = 0
        else:
            dp[i][j] = 左边数量 和 上方路径数量
        '''
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0]*n for _ in range(m)]
        # 初始条件
        for i in range(m):
            if obstacleGrid[i][0] == 1:
                break
            else:
                dp[i][0] = 1
        for i in range(1, n):
            if obstacleGrid[0][i] == 1:
                break
            else:
                dp[0][i] = 1
        # 迭代
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
                
                
        return dp[-1][-1]



# ACM Mode

# import sys

# if __name__ == "__main__":
#     m, n = map(int, sys.stdin.readline().strip().split())
#     k = 