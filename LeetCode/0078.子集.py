# -*- encoding: utf-8 -*-
'''
@File    :   0078.子集.py
@Time    :   2022/06/23 16:12:02
@Author  :   Zhifeng Li
@Contact :   li_zaaachary@163.com
@Desc    :   DFS + 回溯法
给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。

解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。
'''
from typing import List

class Solution:
    '''
    执行用时： 28 ms , 在所有 Python3 提交中击败了 97.45% 的用户 内存消耗： 15.1 MB , 在所有 Python3 提交中击败了 14.56% 的用户
    '''
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.result = [[],]
        self.current = []
        self.nums = nums

        # 此处可以去掉for 改到DFS内
        for index in range(len(nums)):
            self.DFS(index)

        return self.result

    def DFS(self, target):
        self.current.append(self.nums[target])
        self.result.append(self.current[:])
        for i in range(target+1, len(self.nums)):
            self.DFS(i)

        self.current.pop()
        # 此处增加 DFS 的调用 不包含 target的
