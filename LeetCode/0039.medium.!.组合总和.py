# -*- encoding: utf-8 -*-
'''
@File    :   0039.medium.!.组合总和.py
@Time    :   2022/06/24 15:10:41
@Author  :   Zhifeng Li
@Contact :   li_zaaachary@163.com
@Desc    :   

https://leetcode.cn/problems/combination-sum/
'''


class Solution:
    '''
    搜索回溯
    执行用时： 88 ms , 在所有 Python3 提交中击败了 28.74% 的用户 内存消耗： 15.1 MB , 在所有 Python3 提交中击败了 17.23% 的用户
    '''
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.result = []
        self.current = []
        self.current_sum = 0

        self.DFS(candidates, target, 0)
        return self.result
    
    def DFS(self, candidates, target, begin):
        if self.current_sum < target:
            for idx in range(begin, len(candidates)):
                self.current.append(candidates[idx])
                self.current_sum += candidates[idx]
                self.DFS(idx)
                self.current_sum -= self.current.pop()
        elif self.current_sum == target:
            self.result.append(self.current[:])

