# -*- encoding: utf-8 -*-
'''
@File    :   0069.easy.x的平方根.py
@Time    :   2022/07/15 13:51:11
@Author  :   Zhifeng Li
@Contact :   li_zaaachary@163.com
@Desc    :   https://leetcode.cn/problems/sqrtx/
'''

class Solution:
    def mySqrt(self, x: int) -> int:
        '''
        执行用时： 44 ms , 在所有 Python3 提交中击败了 59.49% 的用户 内存消耗： 14.9 MB , 在所有 Python3 提交中击败了 28.14% 的用户
        '''
        left, right = 0, x
        result = 0
        while left <= right:
            mid = left + (right - left) // 2
            temp = mid ** 2
            if temp == x:
                return mid
            elif temp < x:
                result = max(result, mid)
                left = mid + 1
            else:
                right = mid - 1
        
        return result
