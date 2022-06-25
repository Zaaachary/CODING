# -*- encoding: utf-8 -*-
'''
@File    :   0040.medium.!.组合综合II.py
@Time    :   2022/06/24 17:10:03
@Author  :   Zhifeng Li
@Contact :   li_zaaachary@163.com
@Desc    :   https://leetcode.cn/problems/combination-sum-ii/
'''

class Solution:
    '''
    执行用时： 40 ms , 在所有 Python3 提交中击败了 92.06% 的用户 内存消耗： 15 MB , 在所有 Python3 提交中击败了 71.22% 的用户
    '''
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.result = []
        self.current = []
        self.current_sum = 0

        candidates.sort()
        self.DFS(candidates, target, 0)
        return self.result

    def DFS(self, candidates, target, begin):
        if self.current_sum < target:
            for idx in range(begin, len(candidates)):
                if self.current_sum + candidates[idx] > target:
                    break    # 提速，避免额外list操作
                if not (idx > begin and candidates[idx] == candidates[idx-1]):
                    self.current_sum += candidates[idx]
                    self.current.append(candidates[idx])
                    self.DFS(candidates, target, idx + 1)
                    self.current_sum -= candidates[idx]
                    self.current.pop()
        elif self.current_sum == target:
            self.result.append(self.current[:])
