# -*- encoding: utf-8 -*-
'''
@File    :   0704.二分查找.py
@Time    :   2021/12/26 22:40:02
@Author  :   Zhifeng Li
@Contact :   zaaachary_li@163.com
@Desc    :   
给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-search
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List

class Solution:
    '''
    执行用时： 36 ms , 在所有 Python3 提交中击败了 78.89% 的用户
    '''
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            # mid = (left + right)//2
            mid = (right - left) // 2 + left # 防止溢出
            if nums[mid] > target:
                right = mid -1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid
        else:
            return -1
