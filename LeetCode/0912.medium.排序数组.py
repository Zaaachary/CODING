# -*- encoding: utf-8 -*-
'''
@File    :   0912.medium.排序数组.py
@Time    :   2022/07/04 21:34:45
@Author  :   Zhifeng Li
@Contact :   li_zaaachary@163.com
@Desc    :   
'''
from typing import List
import random

class Solution:
    '''
    执行用时： 364 ms , 在所有 Python3 提交中击败了 74.62% 的用户 内存消耗： 20.7 MB , 在所有 Python3 提交中击败了 79.29% 的用户
    '''
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quickSort(nums, 0, len(nums)-1)
        return nums
    
    def quickSort(self, nums: List[int], low: int, high: int):
        if low < high:
            povit_idx = self.partition(nums, low, high)
            self.quickSort(nums, low, povit_idx - 1)
            self.quickSort(nums, povit_idx + 1, high)

    def partition(self, nums, low, high):
        povit_idx = random.randint(low, high)
        povit_item = nums[povit_idx]
        nums[low], nums[povit_idx] = nums[povit_idx], nums[low]

        while low < high:
            while low < high and nums[high] >= povit_item:
                high -= 1
            nums[low] = nums[high]
            while low < high and nums[low] <= povit_item:
                low += 1
            nums[high] = nums[low]

        nums[low] = povit_item

        return low
