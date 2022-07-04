# -*- encoding: utf-8 -*-
'''
@File    :   1901.medium.寻找峰值II.py
@Time    :   2022/06/29 23:13:56
@Author  :   Zhifeng Li
@Contact :   li_zaaachary@163.com
@Desc    :   
'''

class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        '''寻找每行的最大值'''

        m, n = len(mat), len(mat[0])
        up, down = 0, m - 1
        while up <= down:
            mid = up + (down - up) // 2
            mid_max, mid_idx = self.get_rowmax(mat, mid)
            up_num = -1 if 0 > mid -1 else mat[mid-1][mid_idx]
            down_num = -1 if mid + 1 >= m  else mat[mid+1][mid_idx]
            if down_num < mid_max and mid_max > up_num:
                return [mid, mid_idx]
            else:
                up_max = -1 if mid - 1 < 0 else self.get_rowmax(mat, mid - 1)[0]
                down_max = -1 if mid + 1 >= m else self.get_rowmax(mat, mid + 1)[0]
                if up_max > mid_max:
                    down = mid - 1
                else:
                    up = mid + 1

    @staticmethod
    def get_rowmax(mat, i):
        max_idx, max_value = -1, -1
        for j in range(len(mat[i])):
            if mat[i][j] > max_value:
                max_idx = j
                max_value = mat[i][j]
        return max_value, max_idx
            
