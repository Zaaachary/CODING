# -*- encoding: utf-8 -*-
'''
@File    :   0240.medium.搜索二维矩阵II.py
@Time    :   2022/07/06 15:01:39
@Author  :   Zhifeng Li
@Contact :   li_zaaachary@163.com
@Desc    :   
编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target 。该矩阵具有以下特性：

每行的元素从左到右升序排列。
每列的元素从上到下升序排列。
 

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/search-a-2d-matrix-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List

class Solution:
    '''
    分治法，从左下角出发
    '''
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        if n == 0:
            return False

        i = m - 1
        j = 0
        while i >= 0 and j < n:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                j = j + 1
            else:
                i = i - 1
        return False

class Solution_dfs:
    '''
    从 00 开始深度优先搜索，大于target的元素为边界
    执行用时： 188 ms , 在所有 Python3 提交中击败了 22.73% 的用户 内存消耗： 21.7 MB , 在所有 Python3 提交中击败了 5.20% 的用户
    '''
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if matrix[0][0] > target:
            return False
        m, n = len(matrix), len(matrix[0])

        visited = [[False] * n for _ in range(m)]
        return self.DFS(0, 0, visited, matrix, target)
        
    def DFS(self, i, j, visited, matrix, target):
        visited[i][j] = True
        if matrix[i][j] == target:
            return True
        elif matrix[i][j] > target:
            return False
        else:
            if i < len(matrix) - 1 and not visited[i+1][j]:
                if self.DFS(i+1, j, visited, matrix, target):
                    return True
            if j < len(matrix[0]) - 1 and not visited[i][j+1]:
                if self.DFS(i, j+1, visited, matrix, target):
                    return True

class Solution_bs:
    '''
    二分查找确定可能行，再于可能的行中二分查找目标
    执行用时： 160 ms , 在所有 Python3 提交中击败了 89.08% 的用户 内存消耗： 21.3 MB , 在所有 Python3 提交中击败了 22.44% 的用户
    '''
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m - 1
        start, end = 0, m

        while left <= right:
            mid = left + (right - left ) // 2
            temp_l = matrix[mid][0]
            temp_r = matrix[mid][-1]
            if temp_l == target or temp_r == target:
                return True
            elif temp_l > target:
                end = mid
                right = mid - 1
            else:
                if temp_r < target:
                    start = mid
                left = mid + 1
        
        for line in range(start, end):
            left, right = 0, n - 1
            while left <= right:
                mid = left + (right - left) // 2
                temp = matrix[line][mid]
                if temp == target:
                    return True
                elif temp > target:
                    right = mid - 1
                else:
                    left = mid + 1
        else:
            return False

if __name__ == "__main__":
    S = Solution_dfs()
    S.searchMatrix([[1,3,5]], 3)
    