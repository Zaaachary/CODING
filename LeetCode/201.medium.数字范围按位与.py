# -*- encoding: utf-8 -*-
'''
@File    :   201.medium.数字范围按位与.py
@Time    :   2022/06/26 20:39:19
@Author  :   Zhifeng Li
@Contact :   li_zaaachary@163.com
@Desc    :   
给你两个整数 left 和 right ，表示区间 [left, right] ，返回此区间内所有数字 按位与 的结果（包含 left 、right 端点）。
'''

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        result = left
        for num in range(left + 1, right + 1):
            result &= num
        return result

class Solution_leetcode:
    '''
    位运算，找相同 首位的相同非0前缀
    执行用时： 56 ms , 在所有 Python3 提交中击败了 74.67% 的用户 内存消耗： 15 MB , 在所有 Python3 提交中击败了 25.21% 的用户
    '''
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        shift = 0
        while left < right:
            left = left >> 1
            right = right >> 1
            shift += 1
        return left << shift
            