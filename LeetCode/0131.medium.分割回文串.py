# -*- encoding: utf-8 -*-
'''
@File    :   0131.medium.分割回文串.py
@Time    :   2022/07/11 16:38:22
@Author  :   Zhifeng Li
@Contact :   li_zaaachary@163.com
@Desc    :   
https://leetcode.cn/problems/palindrome-partitioning/
https://www.programmercarl.com/0131.%E5%88%86%E5%89%B2%E5%9B%9E%E6%96%87%E4%B8%B2.html
'''
from functools import cache
from typing import List

class Solution:
    '''
    执行用时： 112 ms , 在所有 Python3 提交中击败了 89.19% 的用户 内存消耗： 29.9 MB , 在所有 Python3 提交中击败了 86.90% 的用户
    '''
    def partition(self, s: str) -> List[List[str]]:
        self.path = []
        self.result = []

        self.back_tracing(s, 0)
        return self.result

    def back_tracing(self, s, start_idx):
        if start_idx >= len(s):
            self.result.append(self.path[:])
        else:
            for i in range(start_idx, len(s)):
                temp = s[start_idx:i+1]
                if self.isPalindrome(temp):
                    self.path.append(temp)
                    self.back_tracing(s, i+1)
                    self.path.pop()

    @cache
    @staticmethod
    def isPalindrome(s):
        if not s:
            return False
        left, right = 0, len(s) - 1
        while left <= right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return False
        return True