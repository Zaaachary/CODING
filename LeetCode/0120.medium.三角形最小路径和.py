# -*- encoding: utf-8 -*-
'''
@File    :   0120.medium.三角形最小路径和.py
@Time    :   2022/05/24 20:09:39
@Author  :   Zhifeng Li
@Contact :   li_zaaachary@163.com
@Desc    :   
给定一个三角形 triangle ，找出自顶向下的最小路径和。

每一步只能移动到下一行中相邻的结点上。相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。也就是说，如果正位于当前行的下标 i ，那么下一步可以移动到下一行的下标 i 或 i + 1 。

 triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
11

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/triangle
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from collections import deque

class Solution:
    '''
    自底向上 动态规划
    执行用时： 40 ms , 在所有 Python3 提交中击败了 87.70% 的用户 内存消耗： 15.5 MB , 在所有 Python3 提交中击败了 82.24% 的用户
    '''
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp_list = triangle[-1][:]
        current_len = len(dp_list)
        while current_len > 1:
            print(dp_list)
            for i in range(current_len-1):
                temp_value = triangle[current_len-2][i]
                dp_list[i] = min(dp_list[i], dp_list[i+1]) + temp_value
            dp_list.pop()
            current_len = len(dp_list)

        return dp_list[0]


class Solution_1:
    '''
    DFS 回溯法 超时
    '''
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        self.t_len = len(triangle)
        self.min_path = 10**4 * self.t_len
        self.triangle = triangle
        self.current_path = []

        self.DFS(0, 0)

        return self.min_path
                
    def DFS(self, i, j):
        self.current_path.append(self.triangle[i][j])
        if i == self.t_len - 1:
            self.min_path = min(sum(self.current_path), self.min_path)
        else:
            self.DFS(i+1, j)
            self.DFS(i+1, j+1)

        self.current_path.pop()


class Solution_2:
    '''
    DFS 回溯法 + 剪枝
    '''
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        self.t_len = len(triangle)
        self.min_path = 10**4 * self.t_len
        self.triangle = triangle
        self.current_path = []

        self.DFS(0, 0)

        return self.min_path
                
    def DFS(self, i, j):
        self.current_path.append(self.triangle[i][j])
        current_path_length = sum(self.current_path)

        if current_path_length < self.min_path: # 避免无用路径；此处并不可以，因为节点可以为负值
            if i == self.t_len - 1:
                self.min_path = min(current_path_length, self.min_path)
            else:
                self.DFS(i+1, j)
                self.DFS(i+1, j+1)

        self.current_path.pop()
