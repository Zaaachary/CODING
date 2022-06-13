# -*- encoding: utf-8 -*-
'''
@File    :   0074.medium.搜索二维数组.py
@Time    :   2022/06/07 20:59:43
@Author  :   Zhifeng Li
@Contact :   zaaachary_li@163.com
@Desc    :   
编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：

每行中的整数从左到右按升序排列。
每行的第一个整数大于前一行的最后一个整数。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/search-a-2d-matrix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List

class Solution:
    '''
    执行用时： 32 ms , 在所有 Python3 提交中击败了 91.11% 的用户 内存消耗： 15.2 MB , 在所有 Python3 提交中击败了 56.86% 的用户
    '''
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left, right = 0, len(matrix) - 1
        row = -1
        while left <= right:
            mid = (right - left) // 2 + left
            temp = matrix[mid][0]
            if temp > target:
                right = mid - 1
            else:
                row = mid
                left = mid + 1

        left, right = 0, len(matrix[0]) - 1
        while left <= right:
            mid = (right - left) // 2 + left
            temp = matrix[row][mid]
            if temp == target:
                return True
            elif temp < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False
    
if __name__ == "__main__":
    S = Solution()
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 4
    print(S.searchMatrix(matrix, target))