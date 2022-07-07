# -*- encoding: utf-8 -*-
'''
@File    :   0139.medium.单词拆分.py
@Time    :   2022/07/05 17:54:53
@Author  :   Zhifeng Li
@Contact :   li_zaaachary@163.com
@Desc    :   
'''

from functools import cache

class Solution_memory:
    '''
    记忆化搜索

    执行用时： 40 ms , 在所有 Python3 提交中击败了 85.92% 的用户 内存消耗： 15.4 MB , 在所有 Python3 提交中击败了 5.22% 的用户
    '''
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.wordset = set(wordDict)
        return self.judge(s)
    
    @cache
    def judge(self, s):
        if s in self.wordset:
            return True
        else:
            for i in range(1, len(s)):
                if s[:i] in self.wordset:
                    if self.judge(s[i:]):
                        return True
            else:
                return False


